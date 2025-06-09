from django.core.files.base import ContentFile
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from inboxjournal.models import JournalEntry
from codereviews.models import CodeReviewRequest, CodeAttachment
import json
import base64
import re

@csrf_exempt
def postmark_webhookview(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(['POST'])

    try:
        data = json.loads(request.body)

        sender_email = data.get('FromFull', {}).get('Email', '')
        subject = data.get('Subject', '').lower()
        body = data.get('TextBody', '')
        attachments = data.get('Attachments', [])
        pin_match = re.search(r'pin[:\s]+(\d{4,6})', body, re.IGNORECASE)
        pin = int(pin_match.group(1)) if pin_match else None
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    if 'journal' in subject or 'diary' in subject:
        JournalEntry.objects.create(sender_email=sender_email, content=body, pin=pin)

    elif 'review' in subject or 'inspect' in subject:
        review = CodeReviewRequest.objects.create(
            sender_email=sender_email,
            pr_url=body,
            description='Auto-created from email',  # You might want to parse or customize this
            status='pending'
        )

        for attachment in attachments:
            file_name = attachment.get('Name')
            encoded_content = attachment.get('Content', '')
            if not file_name or not encoded_content:
                continue  # Skip malformed attachments

            decoded_content = base64.b64decode(encoded_content)
            file = ContentFile(decoded_content, name=file_name)

            CodeAttachment.objects.create(
                code_review=review,
                file=file
            )
    else:
        return JsonResponse({'error': 'Subject must include "journal" or "review"'}, status=400)

    return JsonResponse({'message': 'Email processed successfully'}, status=200)

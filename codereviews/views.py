from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import CodeReviewRequest
from django.core.paginator import Paginator

def code_review_list(request):
    reviews = CodeReviewRequest.objects.all().order_by('-created_at')
    paginator = Paginator(reviews, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'codereviews/codereview_list.html', {'page_obj': page_obj})

def code_review_detail(request, pk):
    review = get_object_or_404(CodeReviewRequest, pk=pk)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(CodeReviewRequest.STATUS_CHOICES):
            review.status = new_status
            review.save()
        return redirect('codereviews/codereview_list.html')
    return render(request, 'codereviews/review_detail.html', {'review': review,
                                                              'status_choices': CodeReviewRequest.STATUS_CHOICES,})

@require_POST
def review_update(request, pk):
    review = get_object_or_404(CodeReviewRequest, pk=pk)
    new_status = request.POST.get('status')
    if new_status in dict(CodeReviewRequest.STATUS_CHOICES):
            review.status = new_status
            review.save()
    return redirect('codereview_list')

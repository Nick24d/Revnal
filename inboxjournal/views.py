from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import JournalEntry


def journal_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pin = request.POST.get('pin')

        # Simple check against stored entries
        if JournalEntry.objects.filter(sender_email=email, pin=pin).exists():
            request.session['email'] = email
            request.session['pin'] = pin
            return redirect('journal_dashboard')

        else:
            return redirect('journal_public_list')

    return render(request, 'inboxjournal/login.html')


def journal_public_list(request):
    entries = JournalEntry.objects.filter(pin__isnull=True).order_by('created_at')
    return render(request, 'inboxjournal/public_list.html', {'entries': entries})


def journal_dashboard(request):
    email = request.session.get('email')
    pin = request.session.get('pin')
    if not email or not pin:
        return redirect('journal_public_list')

    entries = JournalEntry.objects.filter(sender_email=email, pin=pin)
    paginator = Paginator(entries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'inboxjournal/dashboard.html', {'page_obj': page_obj})


def journal_detail(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)

    if entry.is_private:
        email = request.session.get('email')
        pin = request.session.get('pin')

        if not email or not pin:
            return redirect('journal_login')

        if entry.sender_email != email or str(entry.pin) != str(pin):
            return redirect('journal_public_list')

    return render(request, 'inboxjournal/details.html', {'entry': entry})


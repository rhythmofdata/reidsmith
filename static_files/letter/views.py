from django.shortcuts import render, redirect

# Create your views here.

from . forms import SubscriberForm, MailMessageForm
from django.contrib import messages  # For actual content of newsletter or message
from django.core.mail import EmailMessage, send_mail  # Allows us to send mail to our recipients
from . models import Subscribers
from django_pandas.io import read_frame


def subscribe(request):
    #If email is valid, then it gets saved into the model.
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Subscription successful!")
            return redirect('/')
    else:
        form = SubscriberForm()
    context = {
        'form': form,
    }
    return render(request, 'subscribe_page.html', context)


def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()

    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message =  form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                "", # Automatically gets host email that was set in settings.py
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the recipient')
            return redirect('mail_letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,

    }
    return render(request, 'mail_letter.html', context)

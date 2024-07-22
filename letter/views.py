
# Code derived from https://www.youtube.com/watch?v=hWtlskOaFNI kenBroTech
#Code derived from https://www.youtube.com/watch?v=LL6qXu8FmVo  Joshyvibe
#Code derived from https://www.youtube.com/watch?v=wl4Yxo5_Cgw Python Lessons
from django.shortcuts import render, redirect
# Create your views here.
from . forms import SubscriberForm, MailMessageForm, letter_from_page_form
from django.contrib import messages  # For actual content of newsletter or message
from django.core.mail import EmailMessage, send_mail  # Allows us to send mail to our recipients
from . models import Subscribers
from django_pandas.io import read_frame
from django.conf import settings
from django.template.loader import render_to_string

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .decorators  import user_is_superuser


def subscribe(request):
    #If email is valid, then it gets saved into the model.
    if request.method == 'POST':
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)

        if not name or not email:
            messages.error(request,"You need to enter a name and a legitimate email in order to subscribe to newsletter")
            return redirect("/")
        
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request,e.messages[0])
            return redirect('/')

        # Check if the email belongs to an existing registered user
        if get_user_model().objects.filter(email=email).exists():
            messages.error(request, f"Found registered user who already has associated {email} email. Log in to subscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/"))
        
        
        # Check if the email is already subscribed
        if Subscribers.objects.filter(email=email).exists():
            messages.error(request, f"{email} address is already a subscribed user.")
            return redirect(request.META.get("HTTP_REFERER", "/"))
        

        # Create a new subscription
        Subscribers.objects.create(name=name, email=email)  #Using create() instead of save()
        messages.success(request, f'{name} Your email {email} has been successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))

    # If the request method is not POST, redirect to the homepage or any other appropriate page
    return render(request,"subscribe_page.html")
        
def index(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():

            Subscribers = form.save()

            context = {'email': Subscribers.email}
            email_content = render_to_string('subscription_thank_you.html',context)

            email_subject = "Thank you for subscribing!"
            recipient_list = [Subscribers.email]
            from_email = settings.EMAIL_HOST_USER


            send_mail(
                email_subject,
                '',
                from_email,
                recipient_list,
                html_message=email_content,
                fail_silently=False
            )

            return render(request,'thank_you_.html',context)
        

    else:
        form = SubscriberForm()
    return render(request, '/',{'form': form})


            
        
'''   
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

'''


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



@user_is_superuser
def letter_from_page(request):
    if request.method == 'POST':
        form = letter_from_page_form(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject,email_message,f"Reid-Smith Family Reunion <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request,"Email sent succesfully")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
            return redirect("/")
    
    form = letter_from_page_form()
    form.fields['receivers'].initial = ','.join([active.email for active in Subscribers.objects.all()])

    return render(request=request, template_name='letter_from_page.html',context={'form':form})
    

    '''
    class NewsletterForm(forms.form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE)'''
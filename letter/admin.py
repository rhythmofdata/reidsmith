from django.contrib import admin
from . models import MailMessage, Subscribers,EmailTemplate
from django import forms
from django.conf import settings
from django.core.mail import send_mail
#from ckeditor.fields import RichTextFormField
from django_ckeditor_5.fields import CKEditor5Field


# Register your models here.

class SubscriberUserAdmin(admin.ModelAdmin):
    list_display= ('email','name','date')

class EmailTemplateAdminForm(forms.ModelForm):
    class Meta:
        model = EmailTemplate
        fields = '__all__'
        widgets = {
            'message': CKEditor5Field(), 

        }

class EmailTemplateAdmin(admin.ModelAdmin):
    form = EmailTemplateAdminForm

    def save_model(self,request,obj,form,change):
        super().save_model(request, obj,form,change)
        subject = obj.subject
        html_message = obj.message

        recipients = [Subscribers.email for Subscribers in obj.recipients.all()]
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject,"",from_email,recipients,fail_silently=False,html_message=html_message)

admin.site.register(MailMessage)
admin.site.register(Subscribers,SubscriberUserAdmin)
admin.site.register(EmailTemplate,EmailTemplateAdmin)

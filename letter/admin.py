from django.contrib import admin
from . models import MailMessage, Subscribers
from django import forms
from django.conf import settings
from django.core.mail import send_mail
from tinymce.models import HTMLField
from django_ckeditor_5.fields import CKEditor5Field


# Register your models here.

class SubscriberUserAdmin(admin.ModelAdmin):
    list_display= ('email','name','date')




admin.site.register(MailMessage)
admin.site.register(Subscribers,SubscriberUserAdmin)


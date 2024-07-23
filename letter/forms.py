from django import forms
from ckeditor.widgets import CKEditorWidget
from . models import Subscribers, MailMessage
from tinymce.widgets import TinyMCE


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields =  ['email', ]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields =  '__all__'



class letter_from_page_form(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")
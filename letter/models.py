from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
#from ckeditor.fields import RichTextField
#from ckeditor_uploader.fields import RichTextUploadingField

# For postgresql
# https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL_Linux.htm

# Create your models here.
class Subscribers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):         # string representation of model
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=100,null=True)
    #message = models.TextField(null=True)
    message = HTMLField(null=True)

    def __str__(self):
        return self.title
    


class EmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    
    #message = CKEditor5Field('Text',config_name='extends')
    message = HTMLField(null=True)
    recipients = models.ManyToManyField(Subscribers)


    def __str__(self):
        return self.subject



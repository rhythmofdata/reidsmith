from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=100,null=True)
    #message = models.TextField(null=True)
    message = HTMLField(null=True)

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.






class Announcement(models.Model):
    name = models.CharField('Announcement Name', max_length= 120)
    announcement_date = models.DateTimeField('Date',default=now)
    #announcement_date = models.DateTimeField(default=now)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

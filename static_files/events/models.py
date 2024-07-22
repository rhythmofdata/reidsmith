
from django.contrib.auth.models import User
from decimal import Decimal
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.


def get_image_filename(instance, filename):
    name = instance.name
    slug = slugify(name)
    return f"products/{slug}-{filename}"

class MyClubUser(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name +' ' + self.last_name
    

class EventTag(models.Model):
    name = models.CharField(
        max_length=100,help_text=_("Designates the name of the tag.")
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self) -> str:
        return self.name
    

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=100)
    address = models.CharField(max_length = 300)
    city = models.CharField('City', blank=True,max_length = 30)
    state = models.CharField('State', blank = True, max_length = 30)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length= 25,blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField("Email", max_length= 50, blank=True)
    owner = models.IntegerField('Venue Owner',blank=False, default=1)

    def __str__(self):
        return self.name


class Event(models.Model):
    event_ticket_type = models.CharField(max_length=50,default="adult")
    age_group = models.CharField(max_length=20, default = "Adult")
    event_price = models.DecimalField(max_digits=5, decimal_places=2,default= 0)
    name = models.CharField('Event Name', max_length= 120)  #modeled from payment sys
    tags = models.ManyToManyField(EventTag, blank=True) #modeled from payment sys
    event_date = models.DateTimeField('Event Date')
    venue =  models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField("Description",blank=True)# modeled from payment sys
    thumbnail = models.ImageField(upload_to=get_image_filename, blank=True)  # from payment sys
    url = models.URLField(blank=True) # from payment sys
    quantity = models.IntegerField(default=1) # from payment sys
    created_at = models.DateTimeField(auto_now=True) #from payment sys
    updated_at = models.DateTimeField(auto_now=True) #from payment sys

    attendees = models.ManyToManyField(MyClubUser,blank=True)
    approved = models.BooleanField("Approved",default=False)
    not_approved = models.BooleanField("Not Approved", default = True) # this is not actually being used yet.  Code logic later.

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    tickets = models.ManyToManyField(Event)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2,default= 0.00)
    
class EventPrice(models.Model):
    event_product = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_price = models.DecimalField(decimal_places=2, max_digits=10)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.event_product.name} {self.event_price}"
    

    

# payment history
class EventPaymentHistory(models.Model):
    PENDING = "P"
    COMPLETED = "C"
    FAILED = "F"

    STATUS_CHOICES = (
        (PENDING, _("pending")),
        (COMPLETED, _("completed")),
        (FAILED, _("failed")),
    )

    email = models.EmailField(max_length = 100,unique=False)
    product = models.ForeignKey(Event, on_delete=models.CASCADE)
    payment_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
    



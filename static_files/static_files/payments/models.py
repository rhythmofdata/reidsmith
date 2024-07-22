from django.db import models
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import events

User = settings.AUTH_USER_MODEL


# Create your models here.

def get_image_filename(instance, filename):
    name = instance.name
    slug = slugify(name)
    return f"products/{slug}-{filename}"



class ProductTag(models.Model):
    name = models.CharField(
        max_length=100,help_text=_("Designates the name of the tag.")
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField(ProductTag, blank=True)
    desc = models.TextField(_("Description"), blank=True)
    thumbnail = models.ImageField(upload_to=get_image_filename, blank=True)
    url = models.URLField(blank=True)
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name

    



class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name} {self.price}"
    


# payment history
class PaymentHistory(models.Model):
    PENDING = "P"
    COMPLETED = "C"
    FAILED = "F"

    STATUS_CHOICES = (
        (PENDING, _("pending")),
        (COMPLETED, _("completed")),
        (FAILED, _("failed")),
    )

    email = models.EmailField(max_length = 100,unique=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

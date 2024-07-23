from django.contrib import admin
from .models import Product, Price, ProductTag, PaymentHistory


class PriceAdmin(admin.StackedInline):
    model = Price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (PriceAdmin,)

    class Meta:
        model = Product

admin.site.register(ProductTag)
admin.site.register(Price)
admin.site.register(PaymentHistory)


class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ['email', 'product', 'payment_status']

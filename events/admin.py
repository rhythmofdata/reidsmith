from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event,EventPrice, Order, EventTag, EventPaymentHistory   #where Event is a product



# Register your models here.

#admin.site.register(Venue)
admin.site.register(MyClubUser)
#admin.site.register(Event)


@admin.register(Venue)
class VenuAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone')
    ordering = ('name',)     #alphabetical
    search_fields = ('name','address')


class EventPriceAdmin(admin.StackedInline):
    model = EventPrice


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_amount',)





@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = (EventPriceAdmin,)
    fields = ('name','venue','event_ticket_type','age_group','event_date','description','manager','approved')
    list_display = ('name', 'event_date','venue','age_group', 'event_price')
    ordering = ('-event_date',)
    search_fields = ('age_group',)

    class Meta:
        model = Event

admin.site.register(EventTag)
admin.site.register(EventPrice)
admin.site.register(EventPaymentHistory)


class EventPaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ['email', 'product', 'payment_status']

#####################################################################################




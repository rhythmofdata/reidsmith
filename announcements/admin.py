from django.contrib import admin

from .models import Announcement

# Register your models here.


#admin.site.register(Announcement)




@admin.register(Announcement)
class EventAdmin(admin.ModelAdmin):
    fields = ('name','announcement_date','description','manager')
    list_display = ('name', 'announcement_date')
    list_filter = ('announcement_date',)
    ordering = ('-announcement_date',)

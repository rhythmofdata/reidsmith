from django.contrib import admin
from .models import Category, BF_Post, Comment, Reply

# Register your models here.
admin.site.register(Category)
#admin.site.register(Author)
admin.site.register(BF_Post)
admin.site.register(Comment)
admin.site.register(Reply)


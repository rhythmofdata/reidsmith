from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib import admin

app = 'letter'

urlpatterns = [
    path('letter_from_page',views.letter_from_page,name="letter_from_page"),
    path('subscribe', views.subscribe, name="subscribe"),
    path('mail-letter', views.mail_letter, name="mail_letter"),
    path('mail-letter', views.index, name="index"),

]
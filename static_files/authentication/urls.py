#https://learndjango.com/tutorials/template-structure   file structure tutorial
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

import os
from django.urls import reverse_lazy


urlpatterns = [
    path('',views.home, name="home"),
    path('signup',views.signUp, name="signup"),
    path('signin',views.signIn, name="signin"),
    path('signout',views.signOut, name="signout"),
    path('update_profile',views.updateProfile, name = "update_profile"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),

    ] 



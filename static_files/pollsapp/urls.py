from django.urls import path

from . import views

urlpatterns = [
    path('polls_home',views.polls_home, name='polls_home'),
    path('vote/<str:pk>', views.vote, name='vote'),
    path('result/<str:pk>', views.result, name='result')
    #path('polls_home', views.polls_home, name='polls_home')
]
from django.urls import path, include
from . import views

# See docs.python.org for datetime and other functionalities

app = 'announcements'

urlpatterns = [
    # int: numbers
    # str: string
    # path: whole urls /  
    # slug: hyphen- and _ underscores  etc
    # uuid: universally unique identifier


    path('announcements/', views.announcements_home, name="announcements-home"),
    path('add_announcement',views.add_announcement, name="add-announcement"),
    path('list_announcements',views.list_announcements, name="list-announcements"),
    #path('announcement-list',views.all_announcements, name="list-announcements"),
    
    #path('add_announcement',views.add_announcement, name="add-announcement"),
    #path('update_announcement/<announcement_id>',views.update_announcement, name='update-announcement'),
    #path('delete_announcement/<announcement_id>',views.delete_announcement, name='delete-announcement'),

    #path('my_announcements',views.my_announcements,name='my-announcements'),
    #path('search_announcements',views.search_announcement,name='search-announcements'),

]
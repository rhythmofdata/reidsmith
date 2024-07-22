from django.urls import path


from . import views

urlpatterns = [
    path('big-forum-home',views.bigForumHome, name='big_forum_home'),
    path('big-forum-posts/<slug>/',views.bigForumPosts, name='big_forum_posts'),
    #path('big-forum-posts/',views.bigForumPosts, name='big_forum_posts'),
    path('big-forum-detail/<slug>/',views.bigForumDetail, name='big_forum_detail'),
    path('big-forum-create-post',views.create_post, name='big_forum_create_post'),
]
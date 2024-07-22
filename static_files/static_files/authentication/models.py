
    

# Create your models here.

# members/models.py
from django.db import models
from django.contrib.auth import get_user_model

#latest
from django.db import models
from django.contrib.auth.models import User

User = get_user_model()


    

'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Adjust the upload_to path as needed

    def __str__(self):
        return f"{self.user.username}'s Profile"
'''



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

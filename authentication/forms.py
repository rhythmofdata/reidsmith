from django import forms
from django.contrib.auth.models import User
from .models import UserProfile



# members/forms.py
from django import forms



"""
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']  # Add more fields as needed
        
        
"""




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic']




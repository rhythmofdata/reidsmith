from django import forms
from django.forms import ModelForm
from .models import Announcement


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        #fields = "__all__"  #Puts all fields on form
        fields = ('name','announcement_date','description')
        labels = {
            'name': '',
            'announcement_date': 'YYYY-MM-DD',
            'description': '',
        }

        #placeholder is a Bootstrap thing
        widgets = {  # this is to style the form
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'AnnouncementName'}),  #forms-control is a boostrap thing
            'announcement_date':forms.TextInput(attrs={'class':'form-control','placeholder':'announcement Date'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})

        }



class AnnouncementFormAdmin(ModelForm):
    class Meta:
        model = Announcement
        #fields = "__all__"  #Puts all fields on form
        fields = ('name','announcement_date','description')
        labels = {
            'name': '',
            'announcement_date': 'YYYY-MM-DD',
            'description': '',
        }
        #placeholder is a Bootstrap thing
        widgets = {  # this is to style the form
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Title of Announcement'}),  #forms-control is a boostrap thing
            'announcement_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Announcement Date'}),
            'manager':forms.Select(attrs={'class':'form-select','placeholder':'Manager'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})

        }

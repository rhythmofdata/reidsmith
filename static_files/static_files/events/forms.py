from django import forms
from django.forms import ModelForm
from .models import Venue, Event


# create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        #fields = "__all__"  #Puts all fields on form
        fields = ('name','address','zip_code','phone','web','email_address')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web':'',
            'email_address': '',
        }
        #placeholder is a Bootstrap thing
        widgets = {  # this is to style the form
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name'}),  #forms-control is a boostrap thing
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
            'web':forms.TextInput(attrs={'class':'form-control','placeholder':'Web Address'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'})

        }




# Adming superuser event form
class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        #fields = "__all__"  #Puts all fields on form
        fields = ('name','event_date','venue','manager','attendees','description')
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD',
            'price':'Price',
            'ticket type':'ticket type',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees':'Attendees',
            'description': '',
        }
        #placeholder is a Bootstrap thing
        widgets = {  # this is to style the form
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'EventName'}),  #forms-control is a boostrap thing
            'event_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}),
            'ticket type':forms.Select(attrs={'class':'form-select','placeholder':'Ticket Type'}),
            'price':forms.DecimalField(decimal_places= 2),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
            'manager':forms.Select(attrs={'class':'form-select','placeholder':'Manager'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})

        }


#user event form

class EventForm(ModelForm):
    class Meta:
        model = Event
        #fields = "__all__"  #Puts all fields on form
        fields = ('name','event_date','venue','attendees','description')
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD',
            'venue': 'Venue',
            'attendees':'Attendees',
            'description': '',
        }
        #placeholder is a Bootstrap thing
        widgets = {  # this is to style the form
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'EventName'}),  #forms-control is a boostrap thing
            'event_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})

        }




        
        
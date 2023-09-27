from django import forms
from django.forms import ModelForm

from .models import Venue, Event

#to Create a Venue from. 
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address',)

        #below code to change the label name from what's given in Venue Model. 
        labels = {
            'name': '', #'' will keep label as empy on VenueForm rendering on html page. Or, you can name something else. 
            'address': '',
            'zip_code': '', 
            'phone': '', 
            'web': '', 
            'email_address': '', 
        }

        #to add class dynamically to each input field in Venue form. 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Venue Name',}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address',}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Zip Code',}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone',}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Website',}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email',}),
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__' #to grap all attributes from the model. 

        labels = {
            'name': '', 
            'event_date': '', 
            'venue': 'Venue:',
            'manager': 'Manager:', 
            'description': '', 
            'attendees': 'Attendees:', 
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Date'}),
            'venue': forms.Select(attrs={'class':'form-control', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class':'form-control', 'placeholder': 'Manager'}),
            'Description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Details'}),

        }
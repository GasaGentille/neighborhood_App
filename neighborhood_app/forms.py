
from .models import Business,Profile,Event,Neighbor
from django import forms

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude= ['user']

class EventForm(forms.ModelForm):
    class Meta:
        model= Event
        exclude=['user']
                

from .models import Business,Profile,Event,Neighbor
from django import forms

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','Profie']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude= ['user']

class EventForm(forms.ModelForm):
    class Meta:
        model= Event
        exclude=['user'] 

class NeighborForm(forms.ModelForm):
    class Meta:
        model : Neighbor
        fields = ['name']
                
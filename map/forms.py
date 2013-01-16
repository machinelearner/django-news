from django import forms
from django.db import models
from map.models import *

class LocationForm(forms.ModelForm):
    """
    Profile location form
    """

    class Meta:
        model = location
        fields = ('location', 'latitude', 'longitude', 'country')


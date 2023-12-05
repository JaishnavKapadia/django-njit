from django import forms
from .models import Location,Building,Feedback

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['from_location', 'to_location']


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['build_name', 'build_img', 'build_description']
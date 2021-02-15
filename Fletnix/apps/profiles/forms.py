from django import forms
from .models import Profiles, WhoIsWatching

class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'

class WhoIsWatchinForm(forms.ModelForm):
    class Meta:
        model = WhoIsWatching
        fields = '__all__'
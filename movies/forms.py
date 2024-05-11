from django import forms
from movies.models import Movies

class movieform(forms.ModelForm):  #Form Definition
    class Meta:
        model=Movies
        fields="__all__"
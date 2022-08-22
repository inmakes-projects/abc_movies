from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
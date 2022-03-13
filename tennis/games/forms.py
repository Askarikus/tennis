from django.contrib.auth.models import User
from django import forms

from .models import Player


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('birth_date', 'country', 'bio')

from django import forms
from .models import Program
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['image', 'name', 'description']


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields  = ('username', 'email', 'password1', 'password2')
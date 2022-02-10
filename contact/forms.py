from attr import fields
from django.forms import ModelForm
from .models import Contacts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        # exclude = ['']
    
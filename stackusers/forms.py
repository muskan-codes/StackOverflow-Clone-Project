from django import forms
from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#Defining all the fields in the Registeration form
class UserRegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
#For updating user profile
#update email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#Update Profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  #In models.py take components of class Profile(phone, bio etc)
        fields = ['bio','phone', 'image'] # fields we want to update
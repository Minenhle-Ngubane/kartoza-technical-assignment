from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import UserProfile

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ["first_name", "last_name", "email"]

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model   = UserProfile
        fields  = "__all__"
        exclude = ["user"]
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from PIL import Image

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['profile_pic', 'date_of_birth']


class UpdateUserForm(forms.ModelForm): 
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


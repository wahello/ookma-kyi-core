from profiles.models import Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateNotificationPreferenceForm(ModelForm):
    """
    A form that lets a user change their notification preferences.
    """
    class Meta:
        model = Profile
        fields = ['notification_preference']

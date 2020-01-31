from characters.models import Character
from django.forms import ModelForm
from django import forms


class CreateCharacterForm(ModelForm):
    name = forms.CharField(
        max_length=32,
        help_text='Enter a name for your character. Warning this cannot be changed latter!')

    class Meta:
        model = Character
        fields = ['name']

from profiles.models import Profile
from django.forms import ModelForm


class UpdateNotificationPreferenceForm(ModelForm):
    """
    A form that lets a user change their notification preferences.
    """
    class Meta:
        model = Profile
        fields = ['notification_preference']

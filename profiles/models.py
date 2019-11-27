from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    """Model representing a single user profile."""

    """The users notification preference, if true will send notifications to the user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notification_preference = models.BooleanField(
        default=False,
        help_text="If ticked will send you notifications."
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

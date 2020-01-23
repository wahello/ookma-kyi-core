from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Character(models.Model):
    """Model representing a single user's character."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=32,
        help_text="Enter a name for your character. Warning this cannot be changed latter!")
    xp = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(9999999)])
    belt = models.ForeignKey('Belt', on_delete=models.CASCADE)
    wins = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(999999)])
    loses = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(999999)])
    draws = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(999999)])


class Belt(models.Model):
    name = models.CharField(
        max_length=32,
        help_text="Belt name"
    )
    belt_image = models.ImageField(upload_to='belts/')
    min_xp = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9999999)],
        help_text="Minimum xp required to obtain belt, 0 for first belt")
    max_xp = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9999999)],
        help_text="Maximum xp for belt")

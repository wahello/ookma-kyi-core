from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    """Model representing a single page."""

    """The page slug, which is used to create url's ex(pages/<slug>)."""
    slug = models.CharField(
        unique=True,
        max_length=20,
        help_text="Enter the slug of the page, this will be the url. Must be unique."
    )

    """The page's title."""
    title = models.CharField(
        max_length=65,
        help_text="Enter the title of the page."
    )

    """The body of the page, with html enabled minus script tags"""
    body = RichTextField(
        help_text="Enter the body of the page, html is allowed"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.slug

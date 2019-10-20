from django.contrib import admin
from pages.models import Page

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Administration object for Page models.
        Defines:
         - fields to be displayed in list view (list_display)
         - orders fields in detail view (fields),
        """
    list_display = ('slug', 'title')

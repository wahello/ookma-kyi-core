from django.contrib import admin
from characters.models import Character

# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    """Administration object for Character models.
        Defines:
         - fields to be displayed in list view (list_display)
         - orders fields in detail view (fields),
        """
    list_display = ('name', 'wins', 'loses', 'draws', 'xp')

from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list_view, name='characters_index'),
]
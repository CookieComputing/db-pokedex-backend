from django.urls import path

from . import views

urlpatterns = [
    path('pokemon_info/', views.find_all_pokemon_info, name='find_all_pokemon_info'),
]
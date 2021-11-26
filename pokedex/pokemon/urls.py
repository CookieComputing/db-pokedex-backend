from django.urls import path

from . import views

urlpatterns = [
    path('pokemon_info/', views.find_all_pokemon_info, name='find_all_pokemon_info'),
    path('pokemon_info/<int:national_num>/', views.find_pokemon_info_by_id, name='find_pokemon_info_by_id'),
    path('pokemon_info/create/', views.create_pokemon_info, name='create_pokemon_info'),
    path('pokemon_info/create/series/', views.create_pokemon_info_series, name='create_pokemon_info_series'),
    path('pokemon_info/update/<int:national_num>/', views.update_pokemon_info, name='update_pokemon_info'),
    path('pokemon_info/delete/<int:national_num>/', views.delete_pokemon_info, name='delete_pokemon_info'),
]
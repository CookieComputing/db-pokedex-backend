from django.urls import path

from . import views

urlpatterns = [
    path('', views.find_all_trainers, name='find_all_trainers'),
    path('<int:trainer_id>/', views.find_trainer_by_id, name='find_trainer_by_id'),
    path('create/', views.create_trainer, name='create_trainer'),
    path('update/<int:trainer_id>/', views.update_trainer, name='update_trainer'),
    path('delete/<int:trainer_id>/', views.delete_trainer, name="delete_trainer"),
    path('teams/', views.find_all_teams, name='find_all_teams'),
    path('teams/<int:trainer_id>/', views.find_all_teams_for_trainer, name='find_all_teams_for_trainer'),
    path('teams/create/', views.create_team, name='create_team'),
    path('teams/update/<int:team_id>/', views.update_team, name='update_team'),
    path('teams/delete/<int:team_id>/', views.delete_team, name='delete_team'),
    path('teams/pokemon/', views.find_all_pokemon, name='find_all_pokemon'),
    path('teams/pokemon/<int:team_id>/', views.find_pokemon_by_team, name='find_pokemon_by_team'),
    path('teams/pokemon/create/', views.create_pokemon, name='create_pokemon'),
    path('teams/pokemon/update/<int:pokemon_id>/', views.update_pokemon, name='update_pokemon'),
    path('teams/pokemon/delete/<int:pokemon_id>/', views.delete_pokemon, name='delete_pokemon'),
    path('pokedex/', views.find_all_pokedexes, name='find_all_pokedexes'),
    path('pokedex/trainer/<int:trainer_id>/', views.find_pokedexes_by_trainer_id, name='find_pokedexes_by_trainer_id'),
    path('pokedex/<int:pokedex_id>/', views.find_pokedex_by_id, name='find_pokedex_by_id'),
    path('pokedex/create/', views.create_pokedex, name='create_pokedex'),
    path('pokedex/update/<int:pokedex_id>/', views.update_pokedex, name='update_pokedex'),
    path('pokedex/delete/<int:pokedex_id>/', views.delete_pokedex, name='delete_pokedex')
]
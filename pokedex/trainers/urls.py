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
]
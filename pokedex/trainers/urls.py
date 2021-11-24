from django.urls import path

from . import views

urlpatterns = [
    path('', views.find_all_trainers, name='find_all_trainers'),
    path('<int:trainer_id>/', views.find_trainer_by_id, name='find_trainer_by_id'),
    path('create/', views.create_trainer, name='create_trainer'),
    path('update/<int:trainer_id>/', views.update_trainer, name='update_trainer'),
    path('delete/<int:trainer_id>/', views.delete_trainer, name="delete_trainer"),
]
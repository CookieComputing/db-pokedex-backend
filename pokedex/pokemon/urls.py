from django.urls import path

from . import views

urlpatterns = [
    path('pokemon_info/', views.find_all_pokemon_info, name='find_all_pokemon_info'),
    path('pokemon_info/<int:national_num>/', views.find_pokemon_info_by_id, name='find_pokemon_info_by_id'),
    path('pokemon_info/create/', views.create_pokemon_info, name='create_pokemon_info'),
    path('pokemon_info/create/series/', views.create_pokemon_info_series, name='create_pokemon_info_series'),
    path('pokemon_info/update/<int:national_num>/', views.update_pokemon_info, name='update_pokemon_info'),
    path('pokemon_info/delete/<int:national_num>/', views.delete_pokemon_info, name='delete_pokemon_info'),

    path('pokemon_type/', views.find_all_pokemon_types, name='find_all_pokemon_types'),
    path('pokemon_type/<int:national_num>/', views.find_all_pokemon_types_by_pokemon_id, name='find_all_pokemon_types_by_pokemon_id'),
    path('pokemon_type/<int:national_num>/<str:type>/', views.find_pokemon_type_by_pokemon_id_and_type, name='find_pokemon_type_by_pokemon_id_and_type'),
    path('pokemon_type/create/', views.create_pokemon_type, name='create_pokemon_type'),
    path('pokemon_type/update/<int:national_num>/<str:type>/', views.update_pokemon_type, name='update_pokemon_type'),
    path('pokemon_type/delete/<int:national_num>/<str:type>/', views.delete_pokemon_type, name='delete_pokemon_type'),
    path('pokemon_type/apply/<int:national_num>/', views.apply_pokemon_types, name='apply_pokemon_types'),

    path('moves/', views.find_all_moves, name='find_all_moves'),
    path('moves/<int:move_id>/', views.find_move_by_id, name='find_move_by_id'),
    path('moves/create/', views.create_move, name='create_move'),
    path('moves/update/<int:move_id>/', views.update_move, name='update_move'),
    path('moves/delete/<int:move_id>/', views.delete_move, name='delete_move'),
    path('moves/pokemon_info/<int:move_id>/', views.find_all_pokemon_info_by_move_id, name='find_all_pokemon_info_by_move_id'),

    path('pokemon_info/moves/', views.find_all_pokemon_moves, name='find_all_pokemon_moves'),
    path('pokemon_info/moves/<int:poke_info_id>/', views.find_all_moves_by_pokemon_info_id, name='find_all_moves_by_pokemon_info_id'),
    path('pokemon_info/moves/associate/', views.associate_poke_info_with_move, name='associate_poke_info_with_move'),
    path('pokemon_info/moves/deassociate/', views.deassociate_poke_info_with_move, name='deassociate_poke_info_with_move'),
]
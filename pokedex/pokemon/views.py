"""
Views/DAOs for Pokemon related tables
"""

from django.http import HttpRequest, HttpResponse

def find_all_pokemon_info(_: HttpRequest) -> HttpResponse:
    return None
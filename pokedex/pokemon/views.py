"""
Views/DAOs for Pokemon related tables
"""
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pokemon.models import PokemonInfo
from utils.serialize import to_json, to_json_one, from_json
from utils.http import assert_post
from typing import Dict, Any
import json

def find_all_pokemon_info(_: HttpRequest) -> HttpResponse:
    pokemon_info = PokemonInfo.objects.all()
    return HttpResponse(to_json(pokemon_info))

def find_pokemon_info_by_id(_: HttpRequest, national_num: int) -> HttpResponse:
    pokemon_info = get_object_or_404(PokemonInfo, pk=national_num)
    return HttpResponse(to_json_one(pokemon_info))

"""
Creates a single pokemon info entry. The evolved_state and devolved_state fields
are optional. To create a series of pokemon info entries that link to each other,
prefer the create_pokemon_info_series() method instead.
"""
@csrf_exempt
def create_pokemon_info(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)

    new_pokemon_info = _create_pokemon_info(post_req)
    return HttpResponse(to_json_one(new_pokemon_info))

"""
Creates a pokemon info entry for each provided pokemon info request. The first
entry is considered the ancestor, while the last entry is the final evolution stage.
Each entry in between will have a devolved and evolved state which are the previous and next
pokemon info entries, respectively.
"""
@csrf_exempt
def create_pokemon_info_series(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    pokemon_info_arr = from_json(request)
    pokemon_info_entries = [_create_pokemon_info(poke_info) for poke_info in pokemon_info_arr]

    if len(pokemon_info_entries) <= 1:
        return HttpResponse(to_json(pokemon_info_entries))
    for i in range(len(pokemon_info_entries)):
        cur_entry = pokemon_info_entries[i]
        if i == 0:
            cur_entry.evolved_state_pkid = pokemon_info_entries[i+1]
        elif i == len(pokemon_info_entries)-1:
            cur_entry.devolved_state_pkid = pokemon_info_entries[i-1]
        else:
            cur_entry.devolved_state_pkid = pokemon_info_entries[i-1]
            cur_entry.evolved_state_pkid = pokemon_info_entries[i+1]
        cur_entry.save()
    return HttpResponse(to_json(pokemon_info_entries))

def _create_pokemon_info(pokemon_info: Dict[str, Any]) -> PokemonInfo:
    evolved_state_pkid = None
    devolved_state_pkid = None
    if 'evolved_state_pkid' in pokemon_info:
        evolved_state_pkid = get_object_or_404(PokemonInfo, pk=pokemon_info['evolved_state_pkid'])
    if 'devolved_state_pkid' in pokemon_info:
        devolved_state_pkid = get_object_or_404(PokemonInfo, pk=pokemon_info['devolved_state_pkid'])
    
    return PokemonInfo.objects.create(
        national_num=pokemon_info['national_num'],
        name=pokemon_info['name'],
        photo_url=pokemon_info['photo_url'],
        description=pokemon_info['description'],
        evolved_state_pkid=evolved_state_pkid,
        devolved_state_pkid=devolved_state_pkid
    )

@csrf_exempt
def update_pokemon_info(request: HttpRequest, national_num: int) -> HttpResponse:
    assert_post(request)
    pokemon_info = get_object_or_404(PokemonInfo, pk=national_num)
    post_req = from_json(request)

    pokemon_info.national_num = post_req.get('national_num', pokemon_info.national_num)
    pokemon_info.name = post_req.get('name', pokemon_info.name)
    pokemon_info.photo_url = post_req.get('photo_url', pokemon_info.photo_url)
    pokemon_info.description = post_req.get('description', pokemon_info.description)
    pokemon_info.evolved_state_pkid = post_req.get('evolved_state_pkid', pokemon_info.evolved_state_pkid)
    pokemon_info.devolved_state_pkid = post_req.get('devolved_state_pkid', pokemon_info.devolved_state_pkid)

    pokemon_info.save()
    return HttpResponse(to_json_one(pokemon_info))

@csrf_exempt
def delete_pokemon_info(request: HttpRequest, national_num: int) -> HttpResponse:
    # Even if there is no data, request should still be a POST
    assert_post(request)

    pokemon_info = get_object_or_404(PokemonInfo, pk=national_num)
    pokemon_info.delete()
    return HttpResponse(json.dumps({}))
"""
Views/DAOs for Pokemon related tables
"""
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pokemon.models import PokemonInfo, PokemonType, Moves, MoveEntry
from utils.serialize import to_json, to_json_one, from_json
from utils.http import assert_post
from typing import Dict, Any
import json

# ===POKEMON_INFO===
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

    pokemon_info.name = post_req.get('name', pokemon_info.name)
    pokemon_info.photo_url = post_req.get('photo_url', pokemon_info.photo_url)
    pokemon_info.description = post_req.get('description', pokemon_info.description)
    
    if 'evolved_state_pkid' in post_req:
        pokemon_info.evolved_state_pkid = get_object_or_404(PokemonInfo, pk=int(post_req['evolved_state_pkid']))
    if 'devolved_state_pkid' in post_req:
        pokemon_info.devolved_state_pkid = get_object_or_404(PokemonInfo, pk=int(post_req['devolved_state_pkid']))
  
    pokemon_info.save()
    return HttpResponse(to_json_one(pokemon_info))

@csrf_exempt
def delete_pokemon_info(request: HttpRequest, national_num: int) -> HttpResponse:
    # Even if there is no data, request should still be a POST
    assert_post(request)

    pokemon_info = get_object_or_404(PokemonInfo, pk=national_num)
    pokemon_info.delete()
    return HttpResponse(json.dumps({}))

# ===POKEMON_TYPE===
def find_all_pokemon_types(_: HttpRequest) -> HttpResponse:
    pokemon_types = PokemonType.objects.all()
    return HttpResponse(to_json(pokemon_types))
    
def find_all_pokemon_types_by_pokemon_id(_: HttpRequest, national_num: int) -> HttpResponse:
    pokemon_types = PokemonType.objects.all(pokemon_info__pk=national_num)
    return HttpResponse(to_json(pokemon_types))

def find_pokemon_type_by_pokemon_id_and_type(_: HttpRequest, national_num: int, type: str) -> HttpResponse:
    pokemon_type = get_object_or_404(PokemonType, type=type, pokemon_info__pk=national_num)
    return HttpResponse(to_json_one(pokemon_type))
    
# The body request should include a national_num identifying which pokemon_info we are looking at 
@csrf_exempt
def create_pokemon_type(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    type_req = from_json(request)
    
    pokemon_info = get_object_or_404(PokemonInfo, pk=type_req['national_num'])
    
    new_type = PokemonType(
        type=type_req['type'],
        pokemon_info=pokemon_info
    )
    new_type.full_clean()
    new_type.save()
    return HttpResponse(to_json_one(new_type))

@csrf_exempt
def update_pokemon_type(request: HttpRequest, national_num: int, type: str) -> HttpResponse:
    assert_post(request)
    pokemon_type = get_object_or_404(PokemonType, type=type, pokemon_info__pk=national_num)
    type_req = from_json(request)
    
    pokemon_type.type = type_req.get('type', pokemon_type.type)

    pokemon_type.full_clean()
    pokemon_type.save()
    return HttpResponse(to_json_one(pokemon_type))

@csrf_exempt
def delete_pokemon_type(request: HttpRequest, national_num: int, type: str) -> HttpResponse:
     # Even if there is no data, request should still be a POST
    assert_post(request)

    pokemon_type = get_object_or_404(PokemonType, type=type, pokemon_info__pk=national_num)
    pokemon_type.delete()
    return HttpResponse(json.dumps({}))
    
# ===MOVES===
def find_all_moves(_: HttpRequest) -> HttpResponse:
    moves = Moves.objects.all()
    return HttpResponse(to_json(moves))

def find_move_by_id(_: HttpRequest, move_id: int) -> HttpResponse:
    move = get_object_or_404(Moves, pk=move_id)
    return HttpResponse(to_json_one(move))

@csrf_exempt
def create_move(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)

    new_move = Moves(
        name=post_req['name'],
        description=post_req['description'],
        element_type=post_req['element_type'],
        move_type=post_req['move_type']
    )
    new_move.full_clean()
    new_move.save()
    return HttpResponse(to_json_one(new_move))

@csrf_exempt
def update_move(request: HttpRequest, move_id: int) -> HttpResponse:
    assert_post(request)
    move = get_object_or_404(Moves, pk=move_id)
    post_req = from_json(request)

    move.name = post_req.get('name', move.name)
    move.description = post_req.get('description', move.description)
    move.element_type = post_req.get('element_type', move.element_type)
    move.move_type = post_req.get('move_type', move.move_type)

    move.full_clean()
    move.save()
    return HttpResponse(to_json_one(move))

@csrf_exempt
def delete_move(request: HttpRequest, move_id: int) -> HttpResponse:
    # Even if there is no data, request should still be a POST
    assert_post(request)

    move = get_object_or_404(Moves, pk=move_id)
    move.delete()
    return HttpResponse(json.dumps({}))

def find_all_pokemon_moves(_: HttpRequest) -> HttpResponse:
    pokemon_moves = MoveEntry.objects.all()
    return HttpResponse(to_json(pokemon_moves))

def find_all_moves_by_pokemon_info_id(_: HttpRequest, poke_info_id: int) -> HttpResponse:
    pokemon_moves = MoveEntry.objects.filter(pokemon_info__national_num=poke_info_id)
    return HttpResponse(to_json(pokemon_moves))

@csrf_exempt
def associate_poke_info_with_move(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)
    poke_info = get_object_or_404(PokemonInfo, pk=post_req['pokemon_info'])
    move = get_object_or_404(Moves, pk=post_req['move'])

    move_entry = MoveEntry(
        pokemon_info=poke_info,
        move=move
    )
    move_entry.full_clean()
    move_entry.save()
    return HttpResponse(to_json_one(move_entry))

@csrf_exempt
def deassociate_poke_info_with_move(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)
    poke_info = get_object_or_404(PokemonInfo, pk=post_req['pokemon_info'])
    move = get_object_or_404(Moves, pk=post_req['move'])
    move_entry = get_object_or_404(MoveEntry, pokemon_info=poke_info, move=move)
    move_entry.delete()
    return HttpResponse(json.dumps({}))
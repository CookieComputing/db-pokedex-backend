"""
Views for trainer related modules. These can be thought of as DAOs for the models.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from pokemon.models import PokemonInfo
from trainers.models import Trainers, Teams, Pokemon, Pokedex, PokedexEntry
from utils.serialize import to_json, to_json_one, to_datetime, from_json
from utils.http import assert_post
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_trainer(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)
    new_trainer = Trainers.objects.create(
        first_name=post_req['first_name'],
        last_name=post_req['last_name'],
        username=post_req['username'],
        password=post_req['password'],
        email=post_req['email'],
    )
    
    if 'date_of_birth' in post_req:
        new_trainer.date_of_birth = to_datetime(post_req['date_of_birth'])
        
    return HttpResponse(to_json_one(new_trainer))

def find_all_trainers(_: HttpRequest) -> HttpResponse:
    trainers = Trainers.objects.all()
    return HttpResponse(to_json(trainers))

def find_trainer_by_id(_: HttpRequest, trainer_id: int) -> HttpResponse:
    trainer = get_object_or_404(Trainers, pk=trainer_id)
    return HttpResponse(to_json_one(trainer))

@csrf_exempt
def update_trainer(request: HttpRequest, trainer_id: int) -> HttpResponse:
    assert_post(request)
    trainer = get_object_or_404(Trainers, pk=trainer_id)
    post_req = from_json(request)

    trainer.first_name = post_req.get('first_name', trainer.first_name)
    trainer.last_name = post_req.get('last_name', trainer.last_name)
    trainer.username = post_req.get('username', trainer.username)
    trainer.password = post_req.get('password', trainer.password)
    trainer.email = post_req.get('email', trainer.email)
    
    if 'date_of_birth' in post_req:
        trainer.date_of_birth = to_datetime(post_req['date_of_birth'])

    trainer.save()
    return HttpResponse(to_json_one(trainer))

@csrf_exempt
def delete_trainer(request: HttpRequest, trainer_id: int) -> HttpResponse:
    # Even if there is no data, request should still be a POST
    assert_post(request)

    trainer = get_object_or_404(Trainers, pk=trainer_id)
    trainer.delete()
    return HttpResponse(json.dumps({}))

def find_all_teams(request: HttpRequest) -> HttpResponse:
    teams = Teams.objects.all()
    return HttpResponse(to_json(teams))

def find_all_teams_for_trainer(request: HttpRequest, trainer_id: int) -> HttpResponse:
    trainer_teams = Teams.objects.filter(trainer__tid=trainer_id)
    return HttpResponse(to_json(trainer_teams))

@csrf_exempt
def create_team(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)
    trainer = get_object_or_404(Trainers, pk=post_req['trainer'])
    new_team = Teams.objects.create(
        name = post_req['name'],
        trainer = trainer
    )
    return HttpResponse(to_json_one(new_team))

@csrf_exempt
def update_team(request: HttpRequest, team_id: int) -> HttpResponse:
    assert_post(request)
    team = get_object_or_404(Teams, pk=team_id)
    post_req = from_json(request)

    team.name = post_req.get('name', team.name)
    team.save()
    return HttpResponse(to_json_one(team))

@csrf_exempt
def delete_team(request: HttpRequest, team_id: int) -> HttpResponse:
    # Even if there is no data, request should still be a POST
    assert_post(request)

    team = get_object_or_404(Teams, pk=team_id)
    team.delete()
    return HttpResponse(json.dumps({}))

def find_all_pokemon(_: HttpRequest) -> HttpResponse:
    pokemon = Pokemon.objects.all()
    return HttpResponse(to_json(pokemon))

def find_pokemon_by_team(_: HttpRequest, team_id: int) -> HttpResponse:
    pokemon = Pokemon.objects.filter(team__id=team_id)
    return HttpResponse(to_json(pokemon))

@csrf_exempt
def create_pokemon(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)
    team = get_object_or_404(Teams, pk=post_req['team'])
    pokemon_info = get_object_or_404(PokemonInfo, pk=post_req['pokemon_info'])

    pokemon = Pokemon(
        nickname = post_req['nickname'],
        gender = post_req['gender'],
        team = team,
        pokemon_info = pokemon_info
    )
    pokemon.full_clean()
    pokemon.save()
    return HttpResponse(to_json_one(pokemon))

@csrf_exempt
def update_pokemon(request: HttpRequest, pokemon_id: int) -> HttpResponse:
    assert_post(request)
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    post_req = from_json(request)

    # Allow name change, gender change, but do not allow team or pokemon info change
    pokemon.nickname = post_req.get('nickname', pokemon.nickname)
    pokemon.gender = post_req.get('gender', pokemon.gender)
    pokemon.full_clean()
    pokemon.save()

    return HttpResponse(to_json_one(pokemon))

@csrf_exempt
def delete_pokemon(request: HttpRequest, pokemon_id: int) -> HttpResponse:
    # Even if there is no data, request should still be a POST
    assert_post(request)
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)

    pokemon.delete()
    return HttpResponse(json.dumps({}))

def find_all_pokedexes(_: HttpRequest) -> HttpResponse:
    pokedexes = Pokedex.objects.all()
    return HttpResponse(to_json(pokedexes))

def find_pokedexes_by_trainer_id(_: HttpRequest, trainer_id: int) -> HttpResponse:
    pokedexes = Pokedex.objects.filter(trainer__tid=trainer_id)
    return HttpResponse(to_json(pokedexes))

def find_pokedex_by_id(_: HttpRequest, pokedex_id: int) -> HttpResponse:
    pokedex = get_object_or_404(Pokedex, pk=pokedex_id)
    return HttpResponse(to_json_one(pokedex))

@csrf_exempt
def create_pokedex(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)
    trainer = get_object_or_404(Trainers, pk=int(post_req['trainer']))
    
    pokedex = Pokedex.objects.create(
        region=post_req['region'],
        trainer=trainer
    )
    pokedex.full_clean()
    return HttpResponse(to_json_one(pokedex))

@csrf_exempt
def update_pokedex(request: HttpRequest, pokedex_id: int) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)
    pokedex = get_object_or_404(Pokedex, pk=pokedex_id)

    pokedex.region = post_req.get('region', pokedex.region)
    pokedex.trainer = post_req.get('trainer', pokedex.trainer)
    pokedex.full_clean()
    pokedex.save()
    return HttpResponse(to_json_one(pokedex))

@csrf_exempt
def delete_pokedex(request: HttpRequest, pokedex_id: int) -> HttpResponse:
    assert_post(request)
    pokedex = get_object_or_404(Pokedex, pk=pokedex_id)

    pokedex.delete()
    return HttpResponse(json.dumps({}))

@csrf_exempt
def associate_pokedex_with_pokemon_info(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)
    
    pokedex = get_object_or_404(Pokedex, pk=post_req['pokedex'])
    pokemon_info = get_object_or_404(PokemonInfo, pk=post_req['pokemon_info'])
    pokedex_entry = PokedexEntry.objects.create(
        pokedex=pokedex,
        pokemon_info=pokemon_info
    )
    return HttpResponse(to_json_one(pokedex_entry))

@csrf_exempt
def deassociate_pokedex_with_pokemon_info(request: HttpRequest) -> HttpResponse:
    assert_post(request)
    post_req = from_json(request)

    pokedex_entry = get_object_or_404(PokedexEntry, pokedex__id=post_req['pokedex'], pokemon_info__national_num=post_req['pokemon_info'])
    pokedex_entry.delete()
    return HttpResponse(json.dumps({}))
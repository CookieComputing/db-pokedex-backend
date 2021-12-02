"""
A Python script which populates the database with sample data for testing purposes.

This script assumes that:
  - There is a backend server running at DB_HOST:8000
  - The backend server can get accessed by its HTTP API endpoints
"""
import environ
import os
import requests
import posixpath
from django.http import HttpResponse
from typing import Dict

env = environ.Env()
environ.Env.read_env("pokedex/pokedex/.env")

DB_HOST = env('DATABASE_HOST')
TRAINER_PREFIX = "trainers"
POKEMON_PREFIX = "pokemon"
POKEMON_INFO_PREFIX = "pokemon_info"
MOVE_PREFIX = "moves"
CREATE = "create"
SERIES = "series"

def main():
    # Create sample trainers
    ash = {
        "first_name": "Ash",
        "last_name": "Ketchum",
        "username": "aketch",
        "password": "pikachu124",
        "email": "ketch.a@husky.neu.edu",
        "date_of_birth": "1984-05-22T00:00:00Z"
    }

    gary = {
        "first_name": "Gary",
        "last_name": "Oak",
        "username": "goak",
        "password": "garyoak123",
        "email": "oak.g@husky.neu.edu",
        "date_of_birth": "1984-04-06T00:00:00Z"
    }
    trainer_path = _format_path(DB_HOST, [TRAINER_PREFIX, CREATE])
    for trainer in [ash, gary]:
        assert_successful_create(trainer_path, trainer)

    # Create sample moves
    scratch = {
        "name": "Scratch",
        "description": "A Normal-type attack. Sharp claws are used to inflict damage on the target.",
        "move_type": "physical",
        "element_type": "normal"
    }

    fire_punch = {
        "name": "Fire Punch",
        "description": "A fiery punch. May cause a burn.",
        "move_type": "physical",
        "element_type": "fire"
    }
    move_path = _format_path(DB_HOST, [POKEMON_PREFIX, MOVE_PREFIX, CREATE])
    for move in [scratch, fire_punch]:
        assert_successful_create(move_path, move)

    # Create sample pokemon info
    # Sample pokemon (non-series)
    geodude = {
        "national_num": 74,
        "name": "geodude",
        "photo_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/074.png",
        "description": "Commonly found near mountain trails and the like. If you step on one by accident, it gets angry.",
    }
    pokemon_info_path = _format_path(DB_HOST, [POKEMON_PREFIX, POKEMON_INFO_PREFIX, CREATE])
    assert_successful_create(pokemon_info_path, geodude)

    # pikachu series
    pikachu_series = [
        {
            "national_num": 172,
            "name": "Pichu",
            "photo_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/172.png",
            "description": "Despite its small size, it can zap even adult humans. However, if it does so, it also surprises itself."
        },
        {
            "national_num": 25,
            "name": "Pikachu",
            "photo_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
            "description": "Pikachu that can generate powerful electricity have cheek sacs that are extra soft and super stretchy."
        },
        {
            "national_num": 26,
            "name": "Raichu",
            "photo_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/026.png",
            "description": "Its long tail serves as a ground to protect itself from its own high-voltage power."
        }
    ]
    pokemon_info_series_path = _format_path(DB_HOST, [POKEMON_PREFIX, POKEMON_INFO_PREFIX, CREATE, SERIES])
    assert_successful_create(pokemon_info_series_path, pikachu_series)

def assert_successful_create(url: str, payload: Dict[str, str]):
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise ValueError("Could not create test data, error code: {}\npayload data: {}".format(response.status_code, payload))

def _format_path(base, components):
    url = "http://{}:8000/".format(base)

    for component in components:
        url = posixpath.join(url, component)
    return url + "/" if url[-1] != "/" else url


if __name__ == "__main__":
    main()
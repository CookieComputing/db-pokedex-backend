"""
Scraper to scan the PokeAPI for information needed to populate our own database with entries about PokemonInfo.
All Pokemon data can be found at https://pokeapi.co/
"""
import json
import requests
from urllib.parse import urljoin
from typing import Union, List
import posixpath

POKEAPI_URL_PREFIX = "https://pokeapi.co/api/v2/"
POKEMON_API_PREFIX = "pokemon/"
POKEMON_MOVE_PREFIX = "move/"
REGION_PREFIX = "region/"
REGIONS = ["Kanto", "Johto", "Hoenn", "Sinnoh", "Unova", "Kalos", "Alola", "Galar"]

def get_pokemon_info(national_num: Union[int, str]) -> dict:
    """
    Retrieve information about a given pokemon through their national number or their name

    :returns: a dictionary containing all API data from the PokeAPI endpoint
    :raises: ValueError if the request failed
    """
    http_query_path = posixpath.join(POKEMON_API_PREFIX, str(national_num))
    api_query = urljoin(POKEAPI_URL_PREFIX, http_query_path)
    response = requests.get(api_query)
    if response.status_code != 200:
        raise ValueError(
            "Error code when requesting Pokemon data: {}, URL attempted: {}".format(response.status_code, api_query))
    return json.loads(response.text)

def get_region(region: Union[int, str]) -> dict:
    """
    Retrieve information about a region supplied as a region number or the name of the region
    
    :returns: a dictionary containing all API data from the PokeAPI endpoint
    :raises: ValueError if the request failed
    """
    http_query_path = posixpath.join(REGION_PREFIX, str(region).lower())
    api_query = urljoin(POKEAPI_URL_PREFIX, http_query_path)
    response = requests.get(api_query)
    if response.status_code != 200:
        raise ValueError(
            "Error code when requesting Region data: {}, URL attempted: {}".format(response.status_code, api_query))
    return json.loads(response.text)

def get_pokemon_in_region(region: Union[int, str]) -> List[dict]:
    """
    Gets all pokemon in a provided region.

    :returns: a list of all pokemon species. Refer to https://pokeapi.co/docs/v2#pokemonspecies
    :raises: ValueError if the request failed or if there is no pokedex in the region
    """
    region = get_region(region)

    # not all regions have a consistent naming scheme: "Kanto" has "kanto" and "updated-kanto", 
    # while "Johto" has "original-johto" and "updated-johto", so it's easier to find the url from the region
    # It looks like the first entry is the oldest, so we'll just use the original pokemon
    pokedex = region['pokedexes'][0]
    pokedex_url = pokedex['url']

    response = requests.get(pokedex_url)
    if response.status_code != 200:
        raise ValueError(
            "Error code when requesting pokedex data: {}, URL attempted: {}".format(response.status_code, pokedex_url))
    
    pokedex_entries = json.loads(response.text)
    pokemon_entries = pokedex_entries['pokemon_entries']

    specimens = []
    for entry in pokemon_entries:
        species_url = entry['pokemon_species']['url']
        response = requests.get(species_url)
        if response.status_code != 200:
            raise ValueError(
                "Error code when requesting species data: {}, URL attempted: {}".format(response.status_code, species_url))
        
        species = json.loads(response.text)
        specimens.append(species)
    return specimens


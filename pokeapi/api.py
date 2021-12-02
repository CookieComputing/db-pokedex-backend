"""
Scraper to scan the PokeAPI for information needed to populate our own database with entries about PokemonInfo.
All Pokemon data can be found at https://pokeapi.co/
"""
import json
import requests
from urllib.parse import urljoin
from typing import Union, List, Dict
import posixpath
import logging
import unidecode

POKEAPI_URL_PREFIX = "https://pokeapi.co/api/v2/"
POKEMON_API_PREFIX = "pokemon/"
POKEMON_MOVE_PREFIX = "move/"
REGION_PREFIX = "region/"
REGIONS = ["Kanto", "Johto", "Hoenn", "Sinnoh", "Unova", "Kalos", "Alola", "Galar"]
logger = logging.getLogger("pokeapi")

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

        # filtering out a few fields which have multiple languages
        def is_eng(x):
            return x['language']['name'] == 'en'
        
        def l_f(arr):
            return list(filter(is_eng, arr))

        species['names'] = l_f(species['names'])
        species['genera'] = l_f(species['genera'])
        species['flavor_text_entries'] = l_f(species['flavor_text_entries'])

        specimens.append(species)
    return specimens


def get_all_moves() -> List[Dict[str, str]]:
    """
    Retrieves move information for all moves in PokeAPI's move API. The resulting list is a
    dictionary formatted to the backend's expectations. Note that this will take a while
    because of the many fetch requests required in each move"""
    move_links = _get_all_move_links()
    return [_get_move(move_link) for move_link in move_links]

def _get_all_move_links() -> List[str]:
    """
    Retrieves all the API endpoint links represented by PokeAPI's move API. The list of strings returned are
    a series of endpoints that can be followed."""

    links = []
    api_query = urljoin(POKEAPI_URL_PREFIX, POKEMON_MOVE_PREFIX)

    def query_data(url):
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(
                "Error code when requesting move data: {}, URL attempted: {}".format(response.status_code, url))
        return json.loads(response.text)
    response = query_data(api_query)

    count = response['count']
    logger.info("{} moves detected from PokeAPI, querying...".format(count))
    while response['next']:
        for move in response['results']:
            links.append(move['url'])
        logger.debug("Currently have {} moves".format(len(links)))
        response = query_data(response['next'])
    return links

def _get_move(move_url: str) -> Dict[str, str]:
    """
    Given a url that points to the move, returns the move and its English attributes.
    """
    response = requests.get(move_url)
    logger.debug("Fetching move from {}".format(move_url))
    if response.status_code != 200:
            raise ValueError(
                "Error code when requesting move data: {}, URL attempted: {}".format(response.status_code, move_url))
    
    move_dict = json.loads(response.text)

    result = {}
    result['name'] = [move_name_obj['name'] for move_name_obj in move_dict['names'] if move_name_obj['language']['name'] == 'en'][0]
    # Some moves are "Max moves" which are represented as None, we'll treat them as special
    result['move_type'] = move_dict['damage_class']['name'] if move_dict['damage_class'] else 'special'
    result['element_type'] = move_dict['type']['name']
    
    # We just pick the first description provided in the PokeAPI
    # since we just need some description
    descriptions = move_dict['flavor_text_entries']
    descriptions = [des for des in descriptions if des['language']['name'] == 'en']
    result['description'] = descriptions[0]['flavor_text'] if descriptions else "This move has no description"

    if result['description']:
        # Unicode has some weird formatting, need to process all excess bits associated
        # with unicode encoding
        result['description'] = unidecode.unidecode(result['description']).replace('\n', ' ')
    return result
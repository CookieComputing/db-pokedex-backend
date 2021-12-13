"""
A Python script which populates the database with sample data for testing purposes.

This script assumes that:
  - There is a backend server running at DB_HOST:8000
  - The backend server can get accessed by its HTTP API endpoints
"""
import common

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
    trainer_path = common.format_path(common.DB_HOST, [common.TRAINER_PREFIX, common.CREATE])
    for trainer in [ash, gary]:
        common.assert_successful_create(trainer_path, trainer)

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

    thunder_punch = {
        "name": "Thunder Punch",
        "description": "An electric punch. It may paralyze.",
        "move_type": "physical",
        "element_type": "electric"
    }

    move_path = common.format_path(common.DB_HOST, [common.POKEMON_PREFIX, common.MOVE_PREFIX, common.CREATE])
    for move in [scratch, fire_punch, thunder_punch]:
        common.assert_successful_create(move_path, move)

    # Create sample pokemon info
    # Sample pokemon (non-series)
    geodude = {
        "national_num": 74,
        "name": "geodude",
        "photo_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/074.png",
        "description": "Commonly found near mountain trails and the like. If you step on one by accident, it gets angry.",
    }
    pokemon_info_path = common.format_path(common.DB_HOST, [common.POKEMON_PREFIX, common.POKEMON_INFO_PREFIX, common.CREATE])
    common.assert_successful_create(pokemon_info_path, geodude)

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
    pokemon_info_series_path = common.format_path(common.DB_HOST, [common.POKEMON_PREFIX, common.POKEMON_INFO_PREFIX, common.CREATE, common.SERIES])
    common.assert_successful_create(pokemon_info_series_path, pikachu_series)

    # Create sample pokemon types
    # Sample types
    # e.g. Geodude (national_num: 74) has two types: rock & ground. Pikachu is an eletric type.
    rock_type = {
        "type": "rock",
        "national_num": 74,
    }
    
    ground_type = {
        "type": "ground",
        "national_num": 74,
    }
    
    electric_type = {
        "type": "electric",
        "national_num": 25,
    }
    pokemon_types_path = common.format_path(common.DB_HOST, [common.POKEMON_PREFIX, common.POKEMON_TYPE_PREFIX, common.CREATE])
    for type in [rock_type, ground_type, electric_type]:
        common.assert_successful_create(pokemon_types_path, type)

    pikachu_knows_scratch = {
        "pokemon_info": 25,
        "move": 1
    }
    geo_dude_knows_fire_punch = {
        "pokemon_info": 74,
        "move": 2
    }
    raichu_knows_scratch = {
        "pokemon_info": 26,
        "move": 1
    }
    raichu_knows_thunder_punch = {
        "pokemon_info": 26,
        "move": 3
    }

    pokemon_move_path = common.format_path(common.DB_HOST, [common.POKEMON_PREFIX, common.POKEMON_INFO_PREFIX, common.MOVE_PREFIX, common.ASSOCIATE])
    for association in [pikachu_knows_scratch, geo_dude_knows_fire_punch, raichu_knows_scratch, raichu_knows_thunder_punch]:
        common.assert_successful_create(pokemon_move_path, association)
    
    # Create pokedexes for Gary and Ash
    ash_kanto = {
        "region": "kanto",
        "trainer": 1
    }
    ash_sinnoh = {
        "region": "sinnoh",
        "trainer": 1
    }
    gary_kanto = {
        "region": "kanto",
        "trainer": 2
    }
    gary_johto = {
        "region": "johto",
        "trainer": 2
    }
    
    pokedex_path = common.format_path(common.DB_HOST, [common.TRAINER_PREFIX, common.POKEDEX_PREFIX, common.CREATE])
    for pokedex_create in [ash_kanto, ash_sinnoh, gary_kanto, gary_johto]:
        common.assert_successful_create(pokedex_path, pokedex_create)

    # Gary and Ash's pokedexes know a bit about some pokemon
    gary_kanto_knows_pichu = {
        "pokedex": 3,
        "pokemon_info": 172
    }
    gary_kanto_knows_raichu = {
        "pokedex": 3,
        "pokemon_info": 26
    }
    ash_kanto_knows_pikachu = {
        "pokedex": 1,
        "pokemon_info": 25
    }
    ash_kanto_knows_geodude = {
        "pokedex": 1,
        "pokemon_info": 74
    }
    ash_sinnoh_knows_geodude = {
        "pokedex": 2,
        "pokemon_info": 74
    }

    pokedex_assoc_path = common.format_path(common.DB_HOST, [common.TRAINER_PREFIX, common.POKEDEX_PREFIX, common.ASSOCIATE])
    for pokedex_assoc in [gary_kanto_knows_pichu, gary_kanto_knows_raichu, ash_kanto_knows_pikachu, ash_kanto_knows_geodude, ash_sinnoh_knows_geodude]:
        common.assert_successful_create(pokedex_assoc_path, pokedex_assoc)

    # Create sample teams for Gary and ash
    ash_team = {
        "name": "Ash's first team",
        "trainer": 1
    }
    gary_team = {
        "name": "Gary's first team",
        "trainer": 2
    }
    team_path = common.format_path(common.DB_HOST, [common.TRAINER_PREFIX, common.TEAMS, common.CREATE])
    for team in [ash_team, gary_team]:
        common.assert_successful_create(team_path, team)

    # Add ash's pikachu, gary's raichu
    pikachu = {
        "nickname": "pikapika",
        "gender": "male",
        "team": 1,
        "pokemon_info": 25
    }
    raichu = {
        "nickname": "raiiii",
        "gender": "female",
        "team": 2,
        "pokemon_info": 26
    }
    pokemon_path = common.format_path(common.DB_HOST, [common.TRAINER_PREFIX, common.TEAMS, common.POKEMON_PREFIX, common.CREATE])
    for pokemon in [pikachu, raichu]:
        common.assert_successful_create(pokemon_path, pokemon)

if __name__ == "__main__":
    main()
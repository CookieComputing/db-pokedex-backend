"""
Models for pokemon related data
"""
from django.db import models

from django.utils.translation import gettext_lazy as _

class PokemonInfo(models.Model):
    national_num = models.IntegerField(primary_key=True)
    evolved_state_pkid = models.ForeignKey('self', models.SET_NULL, db_column='evolved_state_pkid', blank=True, null=True, related_name="evolved_state")
    devolved_state_pkid = models.ForeignKey('self', models.SET_NULL, db_column='devolved_state_pkid', blank=True, null=True, related_name="devolved_state")
    name = models.CharField(max_length=45)
    photo_url = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'pokemon_info'

class ElementTypes(models.TextChoices):
    NORMAL = "normal", _("Normal")
    FIRE = "fire", _("Fire")
    WATER = "water", _("Water")
    ELECTRIC = "electric", _("Electric")
    GRASS = "grass", _("Grass")
    ICE = "ice", _("Ice")
    FIGHTING = "fighting", _("Fighting")
    POISON = "poison", _("Poison")
    GROUND = "ground", _("Ground")
    FLYING = "flying", _("Flying")
    PSYCHIC = "psychic", _("Psychic")
    BUG = "bug", _("Bug")
    ROCK = "rock", _("Rock")
    GHOST = "ghost", _("Ghost")
    DRAGON = "dragon", _("Dragon")
    DARK = "dark", _("Dark")
    STEEL = "steel", _("Steel")
    FAIRY = "fairy", _("Fairy")
    SHADOW = "shadow", _("Shadow") # Shadow is not an official Pokemon type, but does appear in some editions

    class Meta:
        db_table = 'element_types'

class MoveTypes(models.TextChoices):
    PHYSICAL = "physical", _("Physical")
    STATUS = "status", _("Status")
    SPECIAL = "special", _("Special")

    class Meta:
        db_table = 'move_types'

class Moves(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    element_type = models.CharField(max_length=45, choices=ElementTypes.choices)
    move_type = models.CharField(max_length=45, choices=MoveTypes.choices)

    class Meta:
        db_table = 'moves'

class Gender(models.Model):
    """
    Pokemon genders.
    """
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")
    UNKNOWN = "unknown", _("Unknown")

    class Meta:
        db_table = 'genders'

class Region(models.Model):
    """
    The regions that pokemon and trainers reside in.
    """
    KANTO = "kanto", _("Kanto")
    JOHTO = "johto", _("Johto")
    HOENN = "hoenn", _("Hoenn")
    SINNOH = "sinnoh", _("Sinnoh")
    UNOVA = "unova", _("Unova")
    KALOS = "kalos", _("Kalos")
    ALOLA = "alola", _("Alola")
    GALAR = "galar", _("Galar")

    class Meta:
        db_table = 'regions'

class PokemonType(models.Model):
    """
    A many-to-one mapping for a pokemon's type, which can be multiple.
    """
    # Sadly, Django does not have support for multiple primary keys, thus we enforce
    # a unique constraint instead
    type = models.CharField(max_length=45, choices=ElementTypes.choices)
    pokemon_info = models.ForeignKey(PokemonInfo, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'pokemon_types'
        unique_together = (('type', 'pokemon_info'),)

class PokemonWeakness(models.Model):
    """
    A many-to-one mapping for a pokemon's weaknesses, which can be multiple.
    """
    # Sadly, Django does not have support for multiple primary keys, thus we enforce
    # a unique constraint instead
    weakness = models.CharField(max_length=45, choices=ElementTypes.choices)
    pokemon_info = models.ForeignKey(PokemonInfo, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'pokemon_weaknesses'
        unique_together = (('weakness', 'pokemon_info'),)
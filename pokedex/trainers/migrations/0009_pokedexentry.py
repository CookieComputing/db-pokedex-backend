# Generated by Django 3.2.9 on 2021-12-13 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0010_merge_0008_delete_pokemonweakness_0009_moveentry'),
        ('trainers', '0008_alter_pokedex_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokedexEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokedex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.pokedex')),
                ('pokemon_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.pokemoninfo')),
            ],
            options={
                'db_table': 'pokedex_entry',
                'unique_together': {('pokedex', 'pokemon_info')},
            },
        ),
    ]

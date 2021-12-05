# Generated by Django 3.2.9 on 2021-12-04 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0008_auto_20211204_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoveEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.moves')),
                ('pokemon_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.pokemoninfo')),
            ],
            options={
                'db_table': 'move_entries',
                'unique_together': {('pokemon_info', 'move')},
            },
        ),
    ]

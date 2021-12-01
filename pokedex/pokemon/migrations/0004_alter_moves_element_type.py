# Generated by Django 3.2.9 on 2021-12-01 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_moves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moves',
            name='element_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('fire', 'Fire'), ('water', 'Water'), ('electric', 'Electric'), ('grass', 'Grass'), ('ice', 'Ice'), ('fighting', 'Fighting'), ('poison', 'Poison'), ('ground', 'Ground'), ('flying', 'Flying'), ('psychic', 'Psychic'), ('bug', 'Bug'), ('rock', 'Rock'), ('ghost', 'Ghost'), ('dragon', 'Dragon'), ('dark', 'Dark'), ('steel', 'Steel'), ('fairy', 'Fairy'), ('shadow', 'Shadow'), ("<class 'pokemon.models.ElementTypes.Meta'>", 'Meta')], max_length=45),
        ),
    ]
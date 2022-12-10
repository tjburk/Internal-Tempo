# Generated by Django 4.1.2 on 2022-12-10 19:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metronome', '0003_alter_tempo_bpm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempo',
            name='bpm',
            field=models.IntegerField(default=120, null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(10)]),
        ),
    ]

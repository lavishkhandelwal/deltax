# Generated by Django 4.1 on 2022-08-05 16:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("songs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="rate",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(0),
                ],
            ),
        ),
    ]

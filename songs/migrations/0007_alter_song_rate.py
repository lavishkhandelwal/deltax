# Generated by Django 4.1 on 2022-08-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("songs", "0006_song_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="rate",
            field=models.FloatField(default=0),
        ),
    ]

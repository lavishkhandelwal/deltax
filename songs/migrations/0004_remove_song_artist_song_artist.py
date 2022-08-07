# Generated by Django 4.1 on 2022-08-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artists", "0002_artist_rate"),
        ("songs", "0003_alter_song_options_alter_song_cover"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="song",
            name="artist",
        ),
        migrations.AddField(
            model_name="song",
            name="artist",
            field=models.ManyToManyField(blank=True, to="artists.artist"),
        ),
    ]

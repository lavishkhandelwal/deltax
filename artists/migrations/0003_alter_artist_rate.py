# Generated by Django 4.1 on 2022-08-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artists", "0002_artist_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="rate",
            field=models.FloatField(default=0),
        ),
    ]
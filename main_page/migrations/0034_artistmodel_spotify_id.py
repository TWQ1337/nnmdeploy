# Generated by Django 4.0.3 on 2022-06-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0033_albummodel_album_songs_sting'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistmodel',
            name='spotify_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

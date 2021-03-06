# Generated by Django 4.0.3 on 2022-03-28 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_delete_song_songmodel_album_songmodel_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='upcomingalbumentrymodel',
            name='artist_name',
            field=models.ManyToManyField(related_name='upcoming_albums', related_query_name='Upcoming_album', to='main_page.artistmodel'),
        ),
        migrations.AlterField(
            model_name='upcomingalbumentrymodel',
            name='release_date',
            field=models.DateField(default=datetime.date(2022, 3, 29)),
        ),
    ]

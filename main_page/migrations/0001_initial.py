# Generated by Django 4.0.3 on 2022-03-26 11:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('cover64', models.CharField(max_length=150)),
                ('cover320', models.CharField(max_length=150)),
                ('cover640', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('artist_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingAlbumEntryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('release_date', models.DateField(default=datetime.date(2022, 3, 26))),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('cover', models.ImageField(default='cover.jfif', null=True, upload_to='')),
                ('artist_name', models.ManyToManyField(null=True, related_name='upcoming_albums', related_query_name='Upcoming_album', to='main_page.artistmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', related_query_name='song', to='main_page.albummodel')),
                ('artist', models.ManyToManyField(related_name='songs', related_query_name='song', to='main_page.artistmodel')),
            ],
        ),
        migrations.AddField(
            model_name='albummodel',
            name='artist_name',
            field=models.ManyToManyField(related_name='albums', related_query_name='album', to='main_page.artistmodel'),
        ),
    ]

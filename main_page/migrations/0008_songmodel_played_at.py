# Generated by Django 4.0.3 on 2022-03-28 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_songmodel_spotify_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='songmodel',
            name='played_at',
            field=models.CharField(default='bruh', max_length=20),
        ),
    ]

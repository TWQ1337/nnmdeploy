# Generated by Django 4.0.3 on 2022-04-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0023_alter_profilemodel_playlist_albums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listenedsongsmodel',
            name='played_at',
            field=models.CharField(default='bruh', max_length=100),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0032_alter_songmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='albummodel',
            name='album_songs_sting',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0019_encounteredalbummodel_songs_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='reviews_visibility',
            field=models.BooleanField(default=True),
        ),
    ]

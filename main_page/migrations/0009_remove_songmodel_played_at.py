# Generated by Django 4.0.3 on 2022-03-29 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_songmodel_played_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songmodel',
            name='played_at',
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-29 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0009_remove_songmodel_played_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albummodel',
            options={'ordering': ['-release_date']},
        ),
    ]

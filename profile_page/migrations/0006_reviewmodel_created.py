# Generated by Django 4.0.3 on 2022-03-29 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0005_listenedsongsmodel_played_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-21 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0026_alter_songmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingalbumentrymodel',
            name='release_date',
            field=models.DateField(default=datetime.date(2022, 4, 21)),
        ),
    ]

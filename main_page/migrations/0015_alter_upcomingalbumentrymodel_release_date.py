# Generated by Django 4.0.3 on 2022-04-04 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_alter_upcomingalbumentrymodel_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingalbumentrymodel',
            name='release_date',
            field=models.DateField(default=datetime.date(2022, 4, 4)),
        ),
    ]

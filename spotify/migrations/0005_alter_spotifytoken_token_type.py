# Generated by Django 4.0.3 on 2022-03-28 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0004_alter_spotifytoken_token_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='token_type',
            field=models.CharField(default='Bearer', max_length=50),
        ),
    ]

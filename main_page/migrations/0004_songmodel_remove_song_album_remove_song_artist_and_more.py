# Generated by Django 4.0.3 on 2022-03-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_upcomingalbumentrymodel_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.RenameField(
            model_name='albummodel',
            old_name='cover320',
            new_name='cover300',
        ),
        migrations.AlterField(
            model_name='albummodel',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='artistmodel',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='upcomingalbumentrymodel',
            name='album_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

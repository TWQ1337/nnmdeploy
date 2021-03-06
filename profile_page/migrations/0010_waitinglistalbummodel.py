# Generated by Django 4.0.3 on 2022-04-01 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_alter_upcomingalbumentrymodel_release_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_page', '0009_alter_listenedalbummodel_options_likemodel_visible_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaitingListAlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('upcoming_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upcoming_users', related_query_name='upcoming_user', to='main_page.upcomingalbumentrymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waiting_list', related_query_name='waiting_list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['upcoming_album'],
            },
        ),
    ]

# Generated by Django 4.0.3 on 2022-07-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0036_alter_albummodel_name_alter_artistmodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingalbumentrymodel',
            name='cover_link',
            field=models.URLField(blank=True, default='https://uevicgzbyqusuokdtbwi.supabase.co/storage/v1/object/public/nnm-bucket/img_11809-1141319174.png', max_length=400),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_is_stattrack_skins_is_stattrak'),
    ]

    operations = [
        migrations.AddField(
            model_name='skins',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Skin time create'),
        ),
        migrations.AddField(
            model_name='skins',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Skin time update'),
        ),
    ]
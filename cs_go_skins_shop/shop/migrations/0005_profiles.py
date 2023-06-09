# Generated by Django 4.1.7 on 2023-03-02 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_skins_time_create_skins_time_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.TextField(verbose_name='User orders')),
                ('like', models.TextField(verbose_name='User liking skin')),
                ('dislike', models.TextField(verbose_name='User unliking skin')),
                ('favorite', models.TextField(verbose_name='User favorite skin')),
                ('basket', models.TextField(verbose_name='User basket')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

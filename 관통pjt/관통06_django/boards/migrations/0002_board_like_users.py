# Generated by Django 3.2 on 2023-10-20 07:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='like_users',
            field=models.ManyToManyField(related_name='like_board', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2 on 2023-04-29 11:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitterC', '0004_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
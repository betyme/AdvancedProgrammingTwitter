# Generated by Django 4.2 on 2023-05-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterC', '0005_tweet_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

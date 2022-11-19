# Generated by Django 3.2.13 on 2022-11-19 13:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(related_name='review_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
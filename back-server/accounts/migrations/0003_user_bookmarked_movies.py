# Generated by Django 3.2.13 on 2022-11-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmarked_movies',
            field=models.ManyToManyField(related_name='bookmarked_user', to='movies.Movie'),
        ),
    ]

# Generated by Django 3.2 on 2022-11-27 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alter_ego', models.CharField(blank=True, choices=[('AV', 'The Avengers'), ('BA', 'Batman'), ('CA', 'Captain America'), ('FL', 'The Flash'), ('HU', 'The Hulk'), ('IR', 'Iron Man'), ('SP', 'Spiderman'), ('TH', 'Thor'), ('WW', 'Wonder Woman')], default='AN', max_length=2, null=True)),
                ('user_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('user_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('user_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('user_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('user_county', models.CharField(blank=True, max_length=80, null=True)),
                ('user_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

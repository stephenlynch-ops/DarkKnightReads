# Generated by Django 3.2 on 2022-11-27 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0008_alter_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='special_instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
    ]
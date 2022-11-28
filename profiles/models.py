from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):

    ALTER_EGO_ANON = 'AN'
    ALTER_EGO_HULK = 'HU'
    ALTER_EGO_BATMAN = 'BA'
    ALTER_EGO_WONDER_WOMAN = 'WW'
    ALTER_EGO_THOR = 'TH'
    ALTER_EGO_SPIDER_MAN = 'SP'
    ALTER_EGO_AVENGERS = 'AV'
    ALTER_EGO_FLASH = 'FL'
    ALTER_EGO_CAPTAIN_AMERICA = 'CA'
    ALTER_EGO_IRON_MAN = 'IR'
    ALTER_EGO_CHOICES = [
        (ALTER_EGO_ANON, "Pick Your Alter Ego"),
        (ALTER_EGO_AVENGERS, "The Avengers"),
        (ALTER_EGO_BATMAN, "Batman"),
        (ALTER_EGO_CAPTAIN_AMERICA, "Captain America"),
        (ALTER_EGO_FLASH, "The Flash"),
        (ALTER_EGO_HULK, "The Hulk"),
        (ALTER_EGO_IRON_MAN, "Iron Man"),
        (ALTER_EGO_SPIDER_MAN, "Spiderman"),
        (ALTER_EGO_THOR, "Thor"),
        (ALTER_EGO_WONDER_WOMAN, "Wonder Woman"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alter_ego = models.CharField(max_length=2, choices=ALTER_EGO_CHOICES,
                                 default=ALTER_EGO_ANON, null=True, blank=True)
    user_phone_number = models.CharField(max_length=20, null=True, blank=True)
    user_street_address1 = models.CharField(max_length=80, null=True,
                                            blank=True)
    user_street_address2 = models.CharField(max_length=80, null=True,
                                            blank=True)
    user_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    user_postcode = models.CharField(max_length=20, null=True, blank=True)
    user_county = models.CharField(max_length=80, null=True, blank=True)
    user_country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create of update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()

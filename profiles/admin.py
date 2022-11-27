from django.contrib import admin
from .models import UserProfile, Hero

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'alter_ego',
        'user_country',
    )

    ordering = ('id',)


class HeroAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'image',
    )

    ordering = ('name',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Hero, HeroAdmin)

from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'alter_ego',
        'user_country',
    )

    ordering = ('id',)

admin.site.register(UserProfile, UserProfileAdmin)

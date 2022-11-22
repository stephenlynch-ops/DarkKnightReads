from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'asin',
        'title',
        'author',
        'category',
        'publisher',
        'price',
        'hero',
        'image',
    )

    order = ('asin',)


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'name': ('friendly_name',), }

    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

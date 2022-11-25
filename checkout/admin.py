from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'delivery_cost',
                        'order_total', 'grand_total', 'special_gift_active')
    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number', 'country', 'postcode', 
              'town_or_city', 'street_address1', 'street_address2', 'county', 'delivery_cost',
              'order_total', 'special_gift_active', 'special_gift', 'grand_total')
    list_display = ('order_total', 'date', 'full_name', 'order_total', 'delivery_cost', 'grand_total')
    ordering = (-'date',)


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)


admin.site.register(Order, OrderLineItem)

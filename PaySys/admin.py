from django.contrib import admin

from PaySys.models import *


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'until_at')
    list_display_links = ('id', 'name')


class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'percent')
    list_display_links = ('id', 'name')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'currency')
    list_display_links = ('id', 'name')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'paid', 'created_at', )
    list_display_links = ('id', 'name')


admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems)


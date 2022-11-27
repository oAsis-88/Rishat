from django.contrib import admin

from PaySys.forms import *
from PaySys.models import *


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'until_at', )
    list_display_links = ('id', 'name', )


class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'percent', )
    list_display_links = ('id', 'name', )


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'currency', 'quantity', )
    list_display_links = ('id', 'name', )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'paid', 'created_at', )
    list_display_links = ('id', 'name', )


class OrderItemsAdmin(admin.ModelAdmin):
    form = OrderItemsForm
    list_display = ('id', 'order', 'item', 'count', )
    list_display_links = ('id', 'order', 'item', )

    def save_model(self, request, obj, form, change):
        try:
            item_obj = Item.objects.get(name=obj.item.name)
            item_obj.quantity -= obj.count
            item_obj.save()
            return super().save_model(request, obj, form, change)
        except Exception as er:
            pass


admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)


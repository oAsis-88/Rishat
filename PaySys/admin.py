from django.contrib import admin

from PaySys.models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name')


admin.site.register(Item, ItemAdmin)

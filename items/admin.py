from django.contrib import admin
from .models import Item, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price')
    filter_horizontal = ('items',)


admin.site.register(Item)
admin.site.register(Order,OrderAdmin)
# Register your models here.

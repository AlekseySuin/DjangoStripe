from django.contrib import admin
from .models import Item, Order, Tax, Discount


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price')
    filter_horizontal = ('items',)


admin.site.register(Item)
admin.site.register(Order,OrderAdmin)
admin.site.register(Tax)
admin.site.register(Discount)
# Register your models here.

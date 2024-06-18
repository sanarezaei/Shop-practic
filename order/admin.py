from django.contrib import admin
from order.models import ShoppingCard, ShoppingCardLine, Order, OrderLine, Shopping

class ShoppingCardLineInline(admin.TabularInline):
    model = ShoppingCardLine 

class ShoppingCardAdmin(admin.ModelAdmin):
    inlines = [ShoppingCardLineInline]
    
class OrderLineInline(admin.TabularInline):
    model = OrderLine
    
class ShoppingInline(admin.StackedInline):
    model = Shopping
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline, ShoppingInline]
    
admin.site.register(ShoppingCard, ShoppingCardAdmin)
admin.site.register(Order, OrderAdmin)
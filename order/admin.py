from django.contrib import admin
from order.models import ShoppingCard, ShoppingCardLine, Order, OrderLine, Shopping
from payment.models import Payment

class ShoppingCardLineInline(admin.TabularInline):
    model = ShoppingCardLine 

class ShoppingCardAdmin(admin.ModelAdmin):
    inlines = [ShoppingCardLineInline]
    
class OrderLineInline(admin.TabularInline):
    model = OrderLine
    
class ShoppingInline(admin.StackedInline):
    model = Shopping
 
class PaymentInline(admin.TabularInline):
    model = Payment
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline, ShoppingInline, PaymentInline]
    
admin.site.register(ShoppingCard, ShoppingCardAdmin)
admin.site.register(Order, OrderAdmin)
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from product.models import Category, Product, ProductAttribute, ProductImage, Variant, VariantOption, ProductOption
from tinymce import models as tinymce_models

class productImageInline(admin.TabularInline):
    model = ProductImage

class VariantInline(admin.StackedInline):
    model = Variant

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute

class ProductAdmin(admin.ModelAdmin):
    inlines = [productImageInline, ProductAttributeInline, VariantInline]

class VariantOptionInline(admin.TabularInline):
    model = VariantOption
    
class VariantAdmin(admin.ModelAdmin):
    inlines = [VariantOptionInline] 

admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(ProductOption)
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from product.models import Category, Product
from tinymce import models as tinymce_models

admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Product)

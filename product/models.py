from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_models

class Category(MPTTModel):
    title = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']  
        
    class Meta:
        db_table = "categories"
        
    def __str__(self):
        return self.title + (f"({self.parent.title})" if self.parent else "")

class Product(models.Model):
    category = models.ForeignKey("product.Category", verbose_name="Category Product", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField("Product title", max_length=254)
    description = tinymce_models.HTMLField("Product Description")
    
    def __str__(self):
        return f"{self.title} ({self.category})"
    
    
    class Meta:
        db_table = "products"
        
    
    
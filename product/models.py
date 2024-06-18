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
        
    
class ProductImage(models.Model):
    product = models.ForeignKey("product.Product", verbose_name="product", on_delete=models.CASCADE)
    image = models.ImageField("Image")
    
class ProductAttribute(models.Model):
    product = models.ForeignKey("product.Product", verbose_name="product", on_delete=models.CASCADE)
    title = models.CharField("Attribute title", max_length=100)
    value = models.TextField("Attribute value")

class BaseVariant(models.Model):
    product = models.ForeignKey("product.Product", verbose_name="product", on_delete=models.CASCADE)
    title = models.CharField("Variant title", max_length=254)
    price = models.DecimalField("Variant Price", max_digits=10, decimal_places=2)
    
    class Meta:
        abstract = True
    
 
class Variant(BaseVariant):
    sku = models.CharField("Variant SKU", max_length= 50)
    quantity = models.IntegerField("Variant quantity", default=10)
    
    def __str__(self):
        return self.title
    
    
    
class ProductOption(models.Model):
    title = models.CharField("Option title", max_length=254)
    
    def __str__(self):
        return self.title
    
    
class VariantOption(models.Model):
    variant = models.ForeignKey("product.Variant", verbose_name="variant", on_delete=models.CASCADE, null=True)
    option = models.ForeignKey("product.ProductOption", verbose_name="option", on_delete=models.PROTECT)
    value = models.CharField("Variant Option Value", max_length=254)
    
    def __str__(self):
        return f"{self.variant} - {self.option} - {self.value}"
    
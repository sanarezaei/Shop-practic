from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_models
from utils.models.base import TimeStampModel

class Category(MPTTModel, TimeStampModel):
    title = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']  
        
    class Meta:
        db_table = "categories"
        
    def __str__(self):
        return self.title + (f"({self.parent.title})" if self.parent else "")

class Product(TimeStampModel):
    category = models.ForeignKey("product.Category", verbose_name="Category Product", on_delete=models.SET_NULL, null=True, blank=True, related_name="product")
    title = models.CharField("Product title", max_length=254)
    description = tinymce_models.HTMLField("Product Description")
    
    def __str__(self):
        return f"{self.title} ({self.category})"
    
    
    class Meta:
        db_table = "products"
        
    
class ProductImage(TimeStampModel):
    product = models.ForeignKey("product.Product", verbose_name="product", on_delete=models.CASCADE)
    image = models.ImageField("Image")
    
    class Meta:
        db_table = "product_images"
    
class ProductAttribute(TimeStampModel):
    product = models.ForeignKey("product.Product", verbose_name="product", on_delete=models.CASCADE, related_name="attributes")
    title = models.CharField("Attribute title", max_length=100)
    value = models.TextField("Attribute value")
    
    class Meta:
        db_table = "product_attributes"

class BaseVariant(models.Model):
    product = models.ForeignKey("product.Product", verbose_name="product", on_delete=models.CASCADE, related_name="variants")
    title = models.CharField("Variant title", max_length=254)
    price = models.DecimalField("Variant Price", max_digits=10, decimal_places=2)
    
    class Meta:
        abstract = True
    
 
class Variant(BaseVariant, TimeStampModel):
    sku = models.CharField("Variant SKU", max_length= 50)
    quantity = models.IntegerField("Variant quantity", default=10)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "variants"
    
    
class ProductOption(TimeStampModel):
    title = models.CharField("Option title", max_length=254, unique=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "product_options"
    
class VariantOption(TimeStampModel):
    variant = models.ForeignKey("product.Variant", verbose_name="variant", on_delete=models.CASCADE, null=True, related_name="variant_options")
    option = models.ForeignKey("product.ProductOption", verbose_name="option", on_delete=models.PROTECT, db_index=False)
    value = models.CharField("Variant Option Value", max_length=254)
    
    def __str__(self):
        return f"{self.variant} - {self.option} - {self.value}"
    
    class Meta:
        db_table = "variant_options"
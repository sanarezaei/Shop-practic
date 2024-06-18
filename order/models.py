from django.db import models
import uuid
from product.models import BaseVariant
from user.models import BaseAddress

class ShoppingCard(models.Model):
    identifier = models.UUIDField("Unique Identifier", editable=False, default=uuid.uuid4)
    user = models.ForeignKey("user.User", verbose_name="User", on_delete=models.SET_NULL, blank=True, null=True)
    is_primary = models.BooleanField("Is this the primary shopping cart?", default=True)
    
    def save(self, *args, **kwargs):
        if self.is_primary is True and self.user:
            ShoppingCard.objects.filter(user=self.user).update(is_primary=False)
        super().save(*args, **kwargs)
    
    
class ShoppingCardLine(models.Model):
    Shopping_card = models.ForeignKey("order.ShoppingCard", verbose_name="ShoppingCard", on_delete=models.CASCADE)
    variant = models.ForeignKey("product.Variant", verbose_name="Variant", on_delete=models.PROTECT)
    
class Order(models.Model):
    ORDER_STATUS_CREATED = 'craeted'
    ORDER_STATUS_CANCLED = 'cancled'
    ORDER_STATUS_FINISHED = 'finished'
    ORDER_STATUS_PROCCESSED = 'proccessed'
    ORDER_STATUS_SENT = 'sent'
    ORDER_STATUS_DELIVERD = 'deliverd'
    
    ORDER_STATUSES = (
        (ORDER_STATUS_CREATED, 'Order Created'),
        (ORDER_STATUS_CANCLED, 'Order cancled'),
        (ORDER_STATUS_FINISHED, 'Order finished'),
        (ORDER_STATUS_PROCCESSED, 'Order proccessed'),
        (ORDER_STATUS_SENT, 'Order sent'),
        (ORDER_STATUS_DELIVERD, 'deliverd')
    )
    user = models.ForeignKey("user.User", verbose_name="User", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField("Order Status", choices=ORDER_STATUSES, max_length=50)
    
class OrderLine(BaseVariant):
    product = None
    order = models.ForeignKey("order.Order", verbose_name="Order", on_delete=models.CASCADE)
    variant = models.ForeignKey("product.Variant", verbose_name="Variant", on_delete=models.PROTECT)
    
class Shopping(BaseAddress):
    order = models.OneToOneField("order.Order", verbose_name="Order", on_delete=models.CASCADE)
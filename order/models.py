from django.db import models
import uuid
from product.models import BaseVariant
from user.models import BaseAddress
from utils.models.base import TimeStampModel
from django.db.models.functions import TruncDate

class ShoppingCard(TimeStampModel):
    identifier = models.UUIDField("Unique Identifier", editable=False, default=uuid.uuid4)
    user = models.ForeignKey("user.User", verbose_name="User", on_delete=models.SET_NULL, blank=True, null=True, related_name="shopping_card")
    is_primary = models.BooleanField("Is this the primary shopping cart?", default=True)
    
    def save(self, *args, **kwargs):
        if self.is_primary is True and self.user:
            ShoppingCard.objects.filter(user=self.user).update(is_primary=False)
        super().save(*args, **kwargs)
        
    class Meta:
        db_table = "shopping_cards"
    
    
class ShoppingCardLine(TimeStampModel):
    Shopping_card = models.ForeignKey("order.ShoppingCard", verbose_name="ShoppingCard", on_delete=models.CASCADE, related_name="lines")
    variant = models.ForeignKey("product.Variant", verbose_name="Variant", on_delete=models.PROTECT)
    
    class Meta:
        db_table = "shopping_cart_lines"
    
class Order(TimeStampModel):
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
    user = models.ForeignKey("user.User", verbose_name="User", on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    status = models.CharField("Order Status", choices=ORDER_STATUSES, max_length=50)
    
    class Meta:
        db_table = "orders"
        indexes = [models.Index(TruncDate("created_at"), "created_at", name="order_created_at_date_idx")]
class OrderLine(BaseVariant, TimeStampModel):
    product = None
    order = models.ForeignKey("order.Order", verbose_name="Order", on_delete=models.CASCADE, related_name="lines")
    variant = models.ForeignKey("product.Variant", verbose_name="Variant", on_delete=models.PROTECT, related_name="order_lines")
    
    class Meta:
        db_table = "order_lines"
    
class Shopping(BaseAddress, TimeStampModel):
    order = models.OneToOneField("order.Order", verbose_name="Order", on_delete=models.CASCADE, related_name="shippings")
    
    class Meta:
        db_table = "shippings" 
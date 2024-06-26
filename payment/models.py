from django.db import models
from utils.models.base import TimeStampModel
from django.db.models.functions import TruncDate

class Payment(TimeStampModel):
    order = models.ForeignKey("order.Order", verbose_name="Order", on_delete=models.PROTECT, related_name="payments")
    success = models.BooleanField("Is successed")
    tracking_id = models.CharField("Payment Getaway Tracking ID", max_length=100) 
    status = models.CharField("Order Status", max_length=100)
    
    class Meta:
        db_table = "payments"
        indexes = [models.Index(TruncDate("created_at"), "created_at", name="created_at_date_idx")]
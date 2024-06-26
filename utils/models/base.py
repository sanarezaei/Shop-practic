from django.db import models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField("Created At", auto_now_add=True) 
    updated_at = models.DateTimeField("Updated At", auto_now=True)
    
    class Meta:
        abstract = True
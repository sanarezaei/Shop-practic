from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# from utils.models.base import TimeStampedModel

class UserManager(BaseUserManager):
    def create_user(self, phone_no, password=None, **kwargs):
        if not phone_no:
            raise ValueError("Users must have a phone number.")
        user = self.model(
            phone_no=phone_no,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_no, password=None):
        return self.create_user(phone_no, password=password, is_staff=True, is_superuser=True)
    
class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = None
    
    phone_no = models.CharField("Phone number", max_length=20, unique=True)
    
    USERNAME_FIELD = "phone_no"
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    class Meta:
        db_table = 'users'
        
class Profile(models.Model):
    user = models.OneToOneField('user.User', verbose_name="User", on_delete=models.CASCADE, related_name="profile")
    name = models.CharField("Full Name", max_length=100)
    email = models.EmailField("User Email", max_length=254)
    nation_no = models.CharField("Nationality Number", max_length=50)
    birth_date = models.DateField("Birth Date")
    profile_picture = models.ImageField("Profile Picture")
    
    def __str__(self):
        return f"self.name + ({self.user.id})"
    
    class Meta:
        db_table = "Profile"
        
class BaseAddress(models.Model):
    address = models.CharField("User full addresses", max_length=254)
    city = models.CharField("City", max_length=100)
    postal_code = models.CharField("Postal Code", max_length=50)
    recipient_name = models.CharField("Recipient Name", max_length=100)
    latitude = models.DecimalField("Location Latitude", max_digits=10, decimal_places=5)
    longitude = models.DecimalField("Location Longitude", max_digits=10, decimal_places=5)
    
    def __str__(self):
        return f"{self.recipient_name} ({self.city})"
     
    class Meta:
        abstract = True
        
class Address(BaseAddress):
    user = models.ForeignKey("user.User", verbose_name="User", on_delete=models.CASCADE, related_name="addresses", )  
    is_primary = models.BooleanField("Is this the Primary address?", default=False)
           
    def save(self, *args, **kwargs):
        if self.id is None:
            if self.user.addresses.count() == 0:
                self.is_primary = True
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"self.user +({self.postal_code})"
        
    class Meta:
        db_table = "Addresses"
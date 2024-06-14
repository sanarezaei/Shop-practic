from django.contrib import admin
from user.models import Address, Profile, User

admin.site.register(Address)
admin.site.register(Profile)
admin.site.register(User)
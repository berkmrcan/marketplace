from django.contrib import admin
from .models import CustomUser, ShippingAddress
# Register your models here.

admin.register(CustomUser)
admin.register(ShippingAddress)
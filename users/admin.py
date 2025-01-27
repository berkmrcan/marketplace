from django.contrib import admin
from .models import CustomUser, ShippingAddress
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(ShippingAddress)
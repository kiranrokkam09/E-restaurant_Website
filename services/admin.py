from django.contrib import admin
from .models import tablebooking,items,cart

# Register your models here.

admin.site.register(tablebooking)
admin.site.register(items)
admin.site.register(cart)

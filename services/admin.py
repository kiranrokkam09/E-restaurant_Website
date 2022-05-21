from django.contrib import admin
from .models import tablebooking,item,cart,createtable

# Register your models here.

admin.site.register(tablebooking)
admin.site.register(item)
admin.site.register(cart)
admin.site.register(createtable)

from django.contrib import admin
from .models import storeItem, stockItem

# Register your models here.
admin.site.register(storeItem)
admin.site.register(stockItem)
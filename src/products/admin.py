from django.contrib import admin

# Note: this is a relative import:
from .models import Product
# Register your models here.
admin.site.register(Product)

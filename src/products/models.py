from django.db import models

# Create your models here.
# Note: we have to inherit from the default Django class `models.Model`:


class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='This is really cool!Wow')

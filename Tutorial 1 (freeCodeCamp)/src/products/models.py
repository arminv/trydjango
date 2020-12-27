from django.db import models

# Create your models here.
# Note: we have to inherit from the default Django class `models.Model`:


class Product(models.Model):
    # Note `max_length` is a required arg:
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    # Note `blank` only changes the way the field shows/renders, it has nothing to do with the db (whereas `null` has to do with db instead):
    summary = models.TextField(blank=False, null=False)
    # Note `featured` is added later on, so we have two options: null=True and/or default=True
    featured = models.BooleanField()

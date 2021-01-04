from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Owners(models.Model):
    username = models.CharField(max_length=60, verbose_name=_("Name"))

    def __str__(self):
        return self.username

class Pets(models.Model):
    TYPE = (
        (0, _('CAT')),
        (1, _('DOG')),
    )

    types = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_("Type"))
    name = models.CharField(max_length=60, verbose_name=_("Name"))
    owner = models.ForeignKey(
        Owners, on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    img = models.URLField(max_length=600)

    def __str__(self):
        return self.name

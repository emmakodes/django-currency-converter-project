from django.db import models


# Create your models here.
class Currency(models.Model):
    currency_value = models.IntegerField()


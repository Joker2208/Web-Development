from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    qty = models.IntegerField()
    price = models.FloatField()
    brand = models.CharField(max_length=30)
    
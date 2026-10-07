from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 30)
    qty = models.IntegerField()
    price = models.IntegerField()
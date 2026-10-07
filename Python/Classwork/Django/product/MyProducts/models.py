from django.db import models

# Create your models here.
class products(models.Model):
    p_name = models.CharField(max_length = 20)
    qty = models.IntegerField()
    price = models.IntegerField()

    
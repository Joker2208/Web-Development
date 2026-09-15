from django.db import models

class Students(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 60)
    age = models.IntegerField()

class products(models.Model):
    p_name = models.CharField(max_length = 20)
    p_qty = models.IntegerField()
    p_price = models.IntegerField()

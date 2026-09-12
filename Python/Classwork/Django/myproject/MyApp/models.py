from django.db import models

class Students(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 60)
    age = models.IntegerField()
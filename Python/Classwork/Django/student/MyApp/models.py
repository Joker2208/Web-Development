from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=40)
    course = models.CharField(max_length=30)
    grade = models.CharField(max_length=5)
    
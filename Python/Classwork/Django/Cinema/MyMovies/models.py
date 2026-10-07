from django.db import models

# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length = 30)
    rating = models.IntegerField()
    genre = models.CharField(max_length= 20)
    year = models.IntegerField()
    image = models.ImageField(upload_to="image",null=True)
    
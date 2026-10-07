from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)

class Capital(models.Model):
    name = models.CharField(max_length=30)
    country = models.OneToOneField(Country,on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    category  = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    qty = models.IntegerField(null=True)  #null beacause added the field after migrastiong and adding the products in admin so it cannot directly migrate an empty value. it needs a default value or null=true

class Student(models.Model):
    name = models.CharField(max_length=30)

class Course(models.Model):
    name = models.CharField(max_length=30)
    student = models.ManyToManyField(Student)
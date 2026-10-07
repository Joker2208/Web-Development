from django.contrib import admin
from myapp.models import *

# Register your models here.

class Productdisplay(admin.ModelAdmin):
    list_display = ['id','name','price','qty']
    search_fields = ['name']
    list_filter = ['name']

class CapitalDisplay(admin.ModelAdmin):
    list_display = ['id','name']

class CountryDisplay(admin.ModelAdmin):
    list_display = ['id','name']

class Studentdisplay(admin.ModelAdmin):
    list_display = ['id','name']

class CourseDispplay(admin.ModelAdmin):
    list_display = ['id','name']


admin.site.register(Country,CountryDisplay)
admin.site.register(Capital,CapitalDisplay)
admin.site.register(Category)
admin.site.register(Product,Productdisplay)
admin.site.register(Student,Studentdisplay)
admin.site.register(Course,CourseDispplay)

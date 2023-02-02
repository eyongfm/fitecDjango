from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    author = models.CharField(max_length=200,blank=False, default='') 
    price = models.FloatField()   

# Create your models here.

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

class Laptop(models.Model):
    brand=models.CharField(max_length=100)
    price=models.IntegerField()
    processor=models.CharField(max_length=100,null=True)
    

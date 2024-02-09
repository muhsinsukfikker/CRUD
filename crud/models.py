from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self) :
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


    def __str__(self) :
        return self.name




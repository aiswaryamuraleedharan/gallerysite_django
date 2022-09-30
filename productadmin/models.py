from django.db import models

class Product(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=25)
    price=models.DecimalField( max_digits=10, decimal_places=2)

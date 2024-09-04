from django.db import models

class CatFood(models.Model):
    name = models.CharField(max_length = 50)
    flavour = models.CharField(max_length = 10)
    price = models.IntegerField()
    description = models.TextField()
    netto = models.IntegerField()
    category = models.CharField(max_length = 5)
    stock = models.IntegerField()
    expDate = models.DateField()

# Create your models here.

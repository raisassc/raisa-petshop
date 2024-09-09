from django.db import models

class Product(models.Model):
    product_image = models.ImageField(upload_to='product_images/')
    name = models.CharField(max_length=50)
    flavour = models.CharField(max_length=10, default='original')
    price = models.IntegerField()
    description = models.TextField()
    netto = models.IntegerField()
    category = models.CharField(max_length=20)  # Menambah panjang karakter untuk kategori
    stock = models.IntegerField()
    exp_date = models.DateField()
# Create your models here.

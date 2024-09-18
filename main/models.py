import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=50)
    flavour = models.CharField(max_length=10, default='original')
    price = models.IntegerField()
    description = models.TextField()
    netto = models.FloatField()
    category = models.CharField(max_length=20)  # Menambah panjang karakter untuk kategori
    stock = models.IntegerField()
    exp_date = models.DateField()
# Create your models here.

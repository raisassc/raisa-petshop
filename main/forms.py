from django.forms import ModelForm
from main.models import Product

class productForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_image", "name","flavour","price","description", "netto", "category", "stock", "exp_date"]
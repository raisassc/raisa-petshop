from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class productForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_image", "name","flavour","price","description", "netto", "category", "stock", "exp_date"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_flavour(self):
        flavour = self.cleaned_data["flavour"]
        return strip_tags(flavour)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import productForm
from main.models import Product

def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'app': 'Raisa Pet Shop',
        'name': 'Raisa Sakila',
        'class': 'PBP C',
        'product_entries': product_entries,
    }
    return render(request, "main.html", context)

def create_product(request):
    if request.method == "POST":
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = productForm()

    context = {"form": form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data=Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data=Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
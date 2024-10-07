from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.core import serializers
from main.forms import productForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')

# fungsi untuk menampilkan menu

def show_main(request):
    context = {
        'app': 'Raisa Pet Shop',
        'name': request.user.username,
        'npm' : '2306165755',
        'class': 'PBP C',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_product(request):
    if request.method == "POST":
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            print(request.FILES)
            return redirect('main:show_main')
    else:
        form = productForm()
        print(form.errors)

    context = {"form": form}
    return render(request, "create_product.html", context)

#fungsi untuk show xml
def show_xml(request):
    data=Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data=Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
          messages.error(request, "Invalid username or password. Please try again.")

   else:
        form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

#untuk logout user
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get mood entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = productForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get mood berdasarkan id
    eachProduct = Product.objects.get(pk = id)
    # Hapus mood
    eachProduct.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_image = request.FILES.get("product_image")
    name = strip_tags(request.POST.get("name"))
    flavour = strip_tags(request.POST.get("flavour"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    netto = request.POST.get("netto")
    category = strip_tags(request.POST.get("category"))  # Menambah panjang karakter untuk kategori
    stock = request.POST.get("stock")
    exp_date = request.POST.get("exp_date")
    user = request.user

    new_product = Product(
        product_image=product_image, name=name, flavour=flavour, price=price,
        description=description, netto=netto, category=category, stock=stock,exp_date=exp_date,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

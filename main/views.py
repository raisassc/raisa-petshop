from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'Raisa Pet Shop',
        'name' : 'Raisa Sakila',
        'class' : 'PBP C',
    }

    return render(request, "main.html", context)
# Create your views here.
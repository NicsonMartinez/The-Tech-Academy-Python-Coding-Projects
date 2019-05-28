from django.shortcuts import render

from .models import Product

def admin_console(request):
    # this is where we are  gonna store the data from  the datatbase
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})

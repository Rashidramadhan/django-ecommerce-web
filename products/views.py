from django.shortcuts import render
from .forms import Createuser_Form, ProductForm
from .models import Newuser, Product, Order, Product_type
from django.urls import reverse_lazy
# Create your views here.


def test_view(request):
    context = {}
    return render(request, 'index.html', context)

def user_view(request):
    my_form = Createuser_Form()
    if request.method == 'POST':
        my_form = Createuser_Form(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Newuser.objects.create(**my_form.cleaned_data)
            my_form = Createuser_Form()
            success_url = reverse_lazy('login')
    context = {
        'form': my_form
    }
    return render(request, 'signup.html', context)

def product_view(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def display_view(request):
    items = Product.objects.filter('product_code')

    context = {
        'items': items
    }
    return render(request, 'display.html', context)

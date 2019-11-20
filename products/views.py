from django.shortcuts import render
from .models import product


def home(request):
	products = product.objects
	return render(request, "home-page.html", {'products':products})


def checkout(request):

    return render(request, "checkout-page.html")


def products(request):

    return render(request, "product-page.html")

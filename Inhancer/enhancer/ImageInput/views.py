from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home(request):
	return render(request,'ImageInput/dashboard.html')

def products(request):
        return render(request,'ImageInput/products.html')

def customers(request):
        return render(request,'ImageInput/customers.html')


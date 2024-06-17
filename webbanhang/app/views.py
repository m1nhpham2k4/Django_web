from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products} 
    return render(request, 'app/home.html',context)
def card(request):
    context={}
    return render(request,'app/card.html',context)
def checkout(request):
    context = {}
    return render(request,'app/checkout.html',context)
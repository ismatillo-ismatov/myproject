from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    category = Category.objects.all()
    product =  Product.objects.all()
    c = {"category":category,"product":product}
    return render(request,"index.html",c)
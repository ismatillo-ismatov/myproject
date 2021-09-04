from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import Response
from django.views.generic import View
from .forms import CreateUserForm
from .serialazer import ProductSerialazer
from .models import *
import string
from random import choice
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

def get_url():
    url = ''
    llist = [string.ascii_lowercase, string.digits,string.ascii_uppercase]
    for i in range(5):
        url += choice(choice(llist))
    return url

def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    c = {"category":category,"product":product}
    return render(request,"index.html",c)


def loginPage(request):
    if request.method == "POST":
        user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Username yoki Parol xato')
    return render(request, 'login.html',{})

def logoutPage(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    return render(request, 'logout.html')

def signupPage(request):
    form = CreateUserForm()
    if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('blog:login')
    return render(request,'register.html',{'form':form,})

def eltuvchiPage(request):

    return render(request, 'eltuvchi.html')

@login_required(login_url='blog:login')
def offerDetailPage(request, pk):
    product = get_object_or_404(Product, id=pk)
    contex = {
        "product":product
    }
    if request.method == "POST" and not Offer.objects.filter(product=product,vendor=request.user):
        name = request.POST['offername']
        data = Offer(offer_name=name, vendor=request.user, product=product, db_link= get_url())
        data.save()
        print(data)
    return render(request, 'offer_detail.html', contex)

def productDetail(request, slug):
    offer = get_object_or_404(Offer, db_link=slug)
    offer.visits += 1
    offer.save()
    contex = {'offer':offer, 'product':offer.product}
    if request.method == "POST":
        if request.POST['tel']:
            data = request.POST
            user = Order(name=data['ism'], region=data['region'], tel=data['tel'], product=offer.product)
            user.save()
            offer.orders +=1
            offer.visits -= 1
            offer.save()
            messages.info(request, "Tez orada operatorlar aloqaga chiqishadi!")
        else:
            messages.error(request, "Telefon raqam kiritish shart")
    return render(request, 'product_detail.html', contex)
def logoutPage(request):
    logout(request)
    return redirect('blog:index')

def offers(request):
    product = Product.objects.all()
    context = {"product":product}
    return render(request,'offers.html',context)
@api_view(('GET',))
def search_product(request):
    value = request.GET.get("data")
    products = Product.objects.filter(title__icontains=value)
    serial = ProductSerialazer(products,many=True)
    data = {"products":products}
    print(serial.data)
    return Response(serial.data)

def main(request):
    return render("main.html")
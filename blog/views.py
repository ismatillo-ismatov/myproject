from django.shortcuts import render,redirect
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm
from .models import *
# Create your views here.

def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    c = {"category":category,"product":product}
    return render(request,"index.html",c)

class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"
    context_object_name = 'product'

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
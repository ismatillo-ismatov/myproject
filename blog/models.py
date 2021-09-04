from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField('Categoryya',max_length=50)
    slug = models.SlugField('Slug',max_length=50)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField("Nomi",max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='catalog',null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='image',null=True)
    info = models.TextField('Qisqa malumot',blank=True)
    desc = models.TextField(blank=True)
    old_price = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    payment = models.PositiveIntegerField(default=0)
    add_date = models.DateField('Qoshilgan vaqt',auto_now_add=True)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self):
        return self.title

class Offer(models.Model):
    offer_name = models.CharField(max_length=200)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    visits = models.PositiveIntegerField(default=0)
    orders = models.PositiveIntegerField(default=0)
    sold = models.PositiveIntegerField(default=0)
    db_link = models.SlugField(max_length=50)
    def __str__(self):
        return self.offer_name + " - " + self.db_link

class Order(models.Model):
    region = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(verbose_name="Sotildi", default=False, help_text="Sotilgan bo'lsa belgilang!!!")
    def __str__(self):
        return self.tel

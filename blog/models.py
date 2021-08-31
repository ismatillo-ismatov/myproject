from django.db import models


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
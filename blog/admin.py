from django.contrib import admin
from django.contrib.auth.models import User
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug']
    prepopulated_fields = {"slug":('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug','price','id']
    prepopulated_fields = {"slug":('title',)}

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'complete')

admin.site.register(Brand)
admin.site.register(Offer)
admin.site.register(Order, OrdersAdmin)
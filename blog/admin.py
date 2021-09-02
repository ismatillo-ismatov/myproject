from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug']
    prepopulated_fields = {"slug":('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug','price','id']
    prepopulated_fields = {"slug":('title',)}

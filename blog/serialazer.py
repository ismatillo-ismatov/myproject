from  rest_framework import serializers
from .models import *

class ProductSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title','image')
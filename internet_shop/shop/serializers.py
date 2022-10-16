from rest_framework import serializers
from .models import *


class ShopProductSerializer(serializers.ModelSerializer):
    category_name=serializers.CharField(source='cat.name')
    class Meta:
        model=ShopProducts
        fields=('__all__')
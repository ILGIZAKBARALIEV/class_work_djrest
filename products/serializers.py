from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields =  ['id', 'title', 'price', 'created_at']
        # fields = '__all__'
        fields = 'id title price'.split()
        # exclude = 'created_at'.split()



class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
from rest_framework import serializers
from .models import Product,Category,Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'id name created updated'.split()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields =  ['id', 'title', 'price', 'created_at']
        # fields = '__all__'
        fields = 'id title price category tags'.split()
        # depth = 1
        # exclude = 'created_at'.split()




class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many= False)
    tags = TagSerializer(many=True)


    class Meta:
        model = Product
        fields = '__all__'
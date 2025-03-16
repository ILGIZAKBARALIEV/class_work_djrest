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
    category = CategorySerializer(many = False)
    tags = TagSerializer(many=True)
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        # fields =  ['id', 'title', 'price', 'created_at']
        # fields = '__all__'
        fields = 'id title price category  category_name tags tag_names reviews '.split()
        depth = 1
        # exclude = 'created_at'.split()

    def get_category_name(self, product):
        return product.category.name if product.category else None




class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many= False)
    tags = TagSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'

class ProductsValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    text = serializers.CharField(required=False)
    price = serializers.FloatField()
    is_active = serializers.BooleanField()
    category_id = serializers.IntegerField()
    tags = serializers.ListField
from rest_framework import serializers
from .models import Product,Category,Tag
from rest_framework.exceptions import ValidationError


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
    price = serializers.FloatField(min_value= 10, max_value= 10000000000)
    is_active = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField(min_value=1, max_value=100000)
    tags = serializers.ListField(child=serializers.IntegerField(min_value=1),required=False,default=[])

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')
        return category_id

    def validate_tags(self, tags):
        tags_db = Tag.objects.filter(id__in=tags)
        if len(tags) != len(tags_db):
            raise ValidationError('Tags does not exist')
        return tags
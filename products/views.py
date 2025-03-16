from rest_framework.decorators import api_view
from  rest_framework.response import Response
from products.models import Product
from .serializers import ProductSerializer,ProductDetailSerializer,ProductsValidateSerializer
from rest_framework import status
from django.db import transaction

@api_view(http_method_names=['GET','POST'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        # step 1:Collect products from DB (QuerySet)
        products = Product.objects.select_related('category').prefetch_related(
            'tags',
            'reviews'
        ).filter(is_active=True)
        # print(products)
        # step 2: Reformat QuerySet to List of dictionaries (Serializer)
        serializer = ProductSerializer(instance= products, many=True)
        # print(serializer.data)
        # step 3: Return Response(data, status(
        return Response(data= serializer.data)
    elif request.method == 'POST':
        # step 0: Validation (Existing, Typing, Extra)
        serializer = ProductsValidateSerializer(data=request.data)
        if not serializer.is_valid(): #bool
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        # step 1: Receive data from RequestBody
        title = serializer.validated_data.get('title')
        text = serializer.validated_data.get('text')
        price = serializer.validated_data.get('price')
        is_active = serializer.validated_data.get('is_active')
        category_id = serializer.validated_data.get('category')
        tags = serializer.validated_data.get('tags')
        # step 2: Create product by data
        with transaction.atomic():
            product = Product.objects.create(
                title=title,
                text=text,
                price=price,
                is_active=is_active,
                category_id=category_id
            )
            product.tags.set(tags)
            product.save()

        # Product.objects.bulk_create([product, product, product] )
        # step 3: Return response (data=product, status=201)
        return Response(data=ProductDetailSerializer(product).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def procduct_datail_api_view(request, id ):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error':'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductDetailSerializer(product).data
        return Response(data=data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.text = request.data.get('text')
        product.price = request.data.get('price')
        product.is_active = request.data.get('is_active')
        product.category_id = request.data.get('category')
        product.tags.set = request.data.get('tags')
        product.save()
        return Response(data=ProductDetailSerializer(product).data,
                        status=status.HTTP_201_CREATED)

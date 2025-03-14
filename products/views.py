from rest_framework.decorators import api_view
from  rest_framework.response import Response
from products.models import Product
from .serializers import ProductSerializer,ProductDetailSerializer
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
        # step 1: Receive data from RequestBody
        print(request.data)
        # step 2: Create product by data
        # step 3: Return response (data=product, status=201)
        return Response()

@api_view(['GET'])
def procduct_datail_api_view(request, id ):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error':'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product).data

    return Response(data=data)
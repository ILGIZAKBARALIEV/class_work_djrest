from rest_framework.decorators import api_view
from  rest_framework.response import Response
from products.models import Product
from .serializers import ProductSerializer,ProductDetailSerializer
from rest_framework import status

@api_view(http_method_names=['GET'])
def product_list_api_view(request):
    # step 1:Collect products from DB (QuerySet)
    products = Product.objects.select_related('category').prefetch_related(
        'tags',
        'reviews'
    ).filter(is_active=True)
    # print(products)
    # step 2: Reformat QuerySet to List of dictionaries (Serializer)
    serializer = ProductSerializer(instance= products, many=True)
    # print(serializer.data)

    # step 3: Return Response (data, status)
    return Response(data=serializer.data)

@api_view(['GET'])
def procduct_datail_api_view(request, id ):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error':'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product).data

    return Response(data=data)
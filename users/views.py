from django.contrib.auth import authenticate
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def authorization_api_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response({'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'User credentials are wrong '})


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.create_user(username= username , password=password)
    return Response(data = {'user_id':user.id},
                    status = status.HTTP_201_CREATED)

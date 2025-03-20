from django.contrib.auth import authenticate
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import (UserBaseSerializer,
                          UserAuthSerializer,
                          UserRegisterSerializer)
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user= authenticate(**serializer.validated_data) #username = admin1,  password= 123

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
    serializer = UserBaseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.create_user(username= username , password=password,
                                    is_active=False)
    #create code (6-symbol)
    token = Token.objects.create(user=user)
    return Response(data = {'user_id':user.id, 'token':token.key},
                    status = status.HTTP_201_CREATED)

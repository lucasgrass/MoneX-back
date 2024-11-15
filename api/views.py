from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
  UserSerializer,
  UserLoginSerializer
)
import json
from django.http import JsonResponse

class UserCreateView(APIView):
  def post(self, request, *args, **kwargs):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response({
        'message': 'Usuário criado com sucesso!',
      }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({
                    'refresh': str(refresh),
                    'access': access_token
                }, status=status.HTTP_200_OK)
            
            return Response({
                'message': 'Email ou senha inválidos!'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

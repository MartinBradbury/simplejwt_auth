from django.shortcuts import render
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser


class UserRegistrationAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['token'] = {'refresh':str(token), 'access':str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)

class UserLoginAPIView(generics.ListAPIView):
    permission_class = (AllowAny,)
    serializer_class = UserLoginSerializer
    queryset = CustomUser.objects.all()

class UserDetailsAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserDetailsSerializer
    queryset = CustomUser.objects.all()


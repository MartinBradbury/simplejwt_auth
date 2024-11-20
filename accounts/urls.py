from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name="register user"),
    path('login/', UserLoginAPIView.as_view(), name="user login")
]
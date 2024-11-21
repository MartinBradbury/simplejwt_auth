from dj_rest_auth.views import UserDetailsView
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name="register user"),
    path('usr/', UserDetailsAPIView.as_view(), name="user login"),
    path('login/', UserLoginAPIView.as_view(), name="user login"),
]


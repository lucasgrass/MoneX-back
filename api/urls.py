from django.urls import path, include
from .views import (
  UserCreateView,
  UserLoginView
)

urlpatterns = [
  path('users/', UserCreateView.as_view(), name='users-create'),
  path('users/login/', UserLoginView.as_view(), name='users-login'),
]

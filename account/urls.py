from django.urls import path, include
from .api import SignUpAPI, SignInAPI, MainUser

urlpatterns = [
    path('api/auth/register', SignUpAPI.as_view()),
    path('api/auth/login', SignInAPI.as_view()),
    path('api/auth/user', MainUser.as_view()),
]
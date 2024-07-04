from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, UserView

urlpatterns = [
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', TokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='login-refresh'),
    path('auth/me', UserView.as_view(), name='user-info')
]
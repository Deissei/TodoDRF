from django.urls import path
from apps.users.views import UserListAPIView, UserDetailAPIView, UserCreateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/list/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
    path('users/register/', UserCreateAPIView.as_view()),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

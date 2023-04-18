from django.urls import path
from apps.users.views import UserListAPIView, UserDetailAPIView, UserCreateAPIView, RegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>', UserDetailAPIView.as_view()),
    path('create-user/', UserCreateAPIView.as_view()),
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

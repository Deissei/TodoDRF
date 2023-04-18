from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from apps.users.serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer, UserSerializer
from apps.users.models import TodoUser

from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser

class UserListAPIView(ListAPIView):
    model = TodoUser
    queryset = model.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]


class UserDetailAPIView(RetrieveDestroyAPIView):
    queryset = TodoUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminUser]


class UserCreateAPIView(CreateAPIView):
    queryset = TodoUser.objects.all()
    serializer_class = UserCreateSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from apps.todos.permissions import myTodo
from rest_framework.permissions import IsAuthenticated

from apps.todos.models import Todo
from apps.todos.serializers import TodoListSerializer, TodoDetailSerializer, TodoCreateSerializer

class TodoListAPIView(ListAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Todo.objects.filter(author=self.request.user)
        return queryset


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    permission_classes = [myTodo]


class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)



class TodoFinishListAPIView(ListAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Todo.objects.filter(author=self.request.user).filter(is_completed=True)
        return queryset


from django.urls import path
from apps.todos.views import TodoListAPIView, TodoDetailAPIView, TodoCreateAPIView, TodoFinishListAPIView


urlpatterns = [
    path('todo/list/', TodoListAPIView.as_view(), name='list_todo'),
    path('todo/create/', TodoCreateAPIView.as_view(), name='create_todo'),
    path('todo/<int:pk>/', TodoDetailAPIView.as_view(), name='detail_todo'),
    path('todo/finish/', TodoFinishListAPIView.as_view(), name='finish_todo'), 
]

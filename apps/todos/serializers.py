from rest_framework import serializers

from apps.todos.models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'created_at', 'is_completed')


class TodoDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'is_completed', 'created_at', 'image', 'author')



class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'is_completed', 'created_at', 'image', 'author')


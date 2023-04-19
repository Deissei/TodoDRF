from django.db import models
from apps.users.models import TodoUser

class Todo(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='todos')

    author = models.ForeignKey(TodoUser, on_delete=models.CASCADE, related_name='author_todo')

    def __str__(self):
        return self.title

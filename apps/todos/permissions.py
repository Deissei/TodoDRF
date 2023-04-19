from rest_framework.permissions import BasePermission, SAFE_METHODS


class myTodo(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.author == request.user)
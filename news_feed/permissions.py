from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Author'))

    def has_object_permission(self, request, view, obj):
        return bool(request.user and (request.user.id == obj.author.id))
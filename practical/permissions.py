from rest_framework import permissions
from .models import User
from datetime import datetime

permission_list = ["list", "create", "partial_update", 'destroy']


class ProductPermission(permissions.BasePermission):
    # Handle permission for products.

    def has_permission(self, request, view):
        if view.action in permission_list:
            return request.user.is_owner
        elif view.action in ["list"]:
            return request.user.is_owner == False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True


class CategoryPermission(permissions.BasePermission):
    # Handle permission for category.
    def has_permission(self, request, view):
        if view.action in permission_list:
            return request.user.is_owner
        elif view.action in ["list"]:
            return request.user.is_owner == False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True

from rest_framework import permissions
from .models import USER_ROLE_USER, USER_ROLE_ADMIN, USER_ROLE_COACH, USER_ROLE_PLAYER


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == USER_ROLE_ADMIN

class IsPlayerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == USER_ROLE_PLAYER

class IsCoachUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == USER_ROLE_COACH

class IsRegularUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == USER_ROLE_USER
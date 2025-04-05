from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import UserRole


class IsLeagueAdmin(BasePermission):    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == UserRole.LEAGUE_ADMIN

class IsClubAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == UserRole.CLUB_ADMIN

class IsTeamAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == UserRole.TEAM_ADMIN

class IsRegularUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.method in SAFE_METHODS
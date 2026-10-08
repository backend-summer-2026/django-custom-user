from rest_framework import permissions

from .models import User


class IsAdmin(permissions.BasePermission):
    message = 'siz admin emassiz.'

    def has_permission(self, request, view):
        return request.user.role == User.Roles.admin


class IsUser(permissions.BasePermission):
    message = 'siz user emassiz.'

    def has_permission(self, request, view):
        return request.user.role == User.Roles.user


class IsUserOrIsAdmin(permissions.BasePermission):
    message = 'siz user yoki admin emassiz.'

    def has_permission(self, request, view):
        return request.user.role in [User.Roles.user, User.Roles.admin]

from rest_framework.permissions import BasePermission

class TicketsPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'POST'):
            if request.user.is_authenticated:
                return True
            else:
                return False
        else:
            if request.user.is_anonymous:
                return False
            else:
                return request.user.is_staff or request.user.is_superuser
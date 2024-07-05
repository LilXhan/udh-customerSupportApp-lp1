from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            if request.user.is_authenticated:
                return True
            else: 
                return False 
        else:
            return request.user.is_staff
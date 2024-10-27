from rest_framework import permissions


# Permission custom para la api.
# Permite a cualquier usuario, autenticado o no hacer GET.
# Permite todos los otros métodos sólo a usuarios Staff.
class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

from rest_framework import permissions

# Permissions custom para la api.


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Permite que cualquier persona haga un GET y que
    sólo staff tenga acceso a los otros métodos.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsStaffOrAuthenticatedReadOnly(permissions.BasePermission):
    """
    Permite GET de usuarios autenticados
    y acceso completo para staff.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_staff

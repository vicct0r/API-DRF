from rest_framework import permissions

class ESuperUser(permissions.BasePermission):

    def has_permissions(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            else:
                return False
        return True

from rest_framework import permissions

class IsHostOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow hosts of a property to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the host of the property.
        return obj.host == request.user
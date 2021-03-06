from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):

    """ Allows user to edit their own profile """
    def has_object_permission(self, request, view, obj):
        """ CHeck if user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """ CHeck if user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
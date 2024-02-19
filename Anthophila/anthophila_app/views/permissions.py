from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsBeekeeperOrReadOnly(BasePermission):
    """_summary_

    Args:
        BasePermission (IsAuthenticatedOrReadOnly): Only the beekeeper can edit his beeyard or his beehive. 
        For the others, it is read only.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.beekeeper == request.user

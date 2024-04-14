from rest_framework import permissions
from taskite.models.project import ProjectMember

from taskite.exceptions import ProjectPermissionAPIExecption


class ProjectMemberAPIPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.role == 'admin':
            user = ProjectMember.objects.filter(
                user=request.user, project=request.project
            ).first()
            if not user:
                raise ProjectPermissionAPIExecption
        return super().has_permission(request, view)

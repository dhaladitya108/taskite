from rest_framework import permissions
from taskite.models.project import ProjectMember

from taskite.exceptions import ProjectPermissionAPIException


class ProjectMemberAPIPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_superuser:
            project_member = ProjectMember.objects.filter(
                user=request.user, project=request.project
            ).first()
            if not project_member:
                raise ProjectPermissionAPIException

            request.project_role = project_member.role
        else:
            request.project_role = "admin"
        return super().has_permission(request, view)

from taskite.models import Project, User
from rest_framework.exceptions import APIException
from rest_framework import status

from taskite.exceptions import ProjectNotFoundAPIException


class ProjectFetchMixin:
    def get_project(self):
        project_id = self.kwargs.get("project_id")
        project = Project.objects.filter(id=project_id).first()
        if not project:
            raise ProjectNotFoundAPIException
        return project

    def dispatch(self, request, *args, **kwargs):
        request.project = self.get_project()
        return super().dispatch(request, *args, **kwargs)

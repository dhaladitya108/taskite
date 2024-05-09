import humps
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import Http404

from taskite.models import Project, User, State, Task
from taskite.serializers import ProjectSerializer


class ProjectDetailView(LoginRequiredMixin, View):
    def get(self, request, slug):
        project = Project.objects.filter(slug=slug).first()
        if not project:
            raise Http404()
        context = {
            "props": {
                "project": ProjectSerializer(project).data,
            }
        }
        return render(request, "projects/detail.html", context)


class ProjectTaskView(LoginRequiredMixin, View):
    def get(self, request, slug, task_id):
        project = Project.objects.filter(slug=slug).first()
        if not project:
            raise Http404()

        task = Task.objects.filter(project=project, task_id=task_id).first()
        if not task:
            raise Http404()

        context = {
            "props": {"project": ProjectSerializer(project).data, "task_id": task.id}
        }
        return render(request, "projects/task.html", context)


class ProjectSettingsGeneralView(LoginRequiredMixin, View):
    def get(self, request, slug):
        project = Project.objects.filter(slug=slug).first()
        if not project:
            raise Http404()

        serializer = ProjectSerializer(project)
        
        context = {"props": {"project": humps.camelize(serializer.data)}}
        return render(request, "projects/settings/general.html", context)


class ProjectSettingsMembersView(LoginRequiredMixin, View):
    def get(self, request, slug):
        project = Project.objects.filter(slug=slug).first()
        if not project:
            raise Http404()
        
        serializer = ProjectSerializer(project)
        
        context = {"props": {"project": humps.camelize(serializer.data)}}
        return render(request, "projects/settings/members.html", context)

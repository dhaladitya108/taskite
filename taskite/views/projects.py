import humps
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import Http404
from django.utils import timezone

from taskite.models import Project, Task, ProjectMember, ProjectInvite
from taskite.serializers import ProjectSerializer


class ProjectListView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "projects/list.html")


class ProjectDetailView(LoginRequiredMixin, View):
    def get(self, request, slug):
        project = Project.objects.filter(slug=slug).first()
        if not project:
            raise Http404()

        serializer = ProjectSerializer(project)
        context = {
            "props": {
                "project": humps.camelize(serializer.data),
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

        project_member = ProjectMember.objects.filter(
            project=project, user=request.user
        ).first()
        if not project_member:
            raise Http404()

        serializer = ProjectSerializer(project)

        context = {
            "props": {
                "project": humps.camelize(serializer.data),
                "role": project_member.role,
            }
        }
        return render(request, "projects/settings/general.html", context)


class ProjectSettingsMembersView(LoginRequiredMixin, View):
    def get(self, request, slug):
        project = Project.objects.filter(slug=slug).first()
        if not project:
            raise Http404()

        project_member = ProjectMember.objects.filter(
            project=project, user=request.user
        ).first()
        if not project_member:
            raise Http404()

        serializer = ProjectSerializer(project)

        context = {
            "props": {
                "project": humps.camelize(serializer.data),
                "role": project_member.role,
            }
        }
        return render(request, "projects/settings/members.html", context)


class ProjectInviteConfirmationView(LoginRequiredMixin, View):
    def get(self, request, project_invite_id):
        project_invite = ProjectInvite.objects.filter(
            id=project_invite_id,
            email=request.user.email,
            confirmed_at__isnull=True,
        ).first()
        if not project_invite:
            raise Http404()

        project_invite.confirmed_at = timezone.now()
        project_invite.save(update_fields=["confirmed_at"])
        try:
            ProjectMember.objects.create(
                user=request.user,
                project=project_invite.project,
                role=project_invite.role,
                joined_at=timezone.now(),
            )
        except Exception:
            print("Failed to create a project member")

        return redirect("project-detail", slug=project_invite.project.slug)


class ProjectInviteRejectionView(LoginRequiredMixin, View):
    def get(self, request, project_invite_id):
        project_invite = ProjectInvite.objects.filter(
            id=project_invite_id,
            email=request.user.email,
            confirmed_at__isnull=True,
        ).first()
        if not project_invite:
            raise Http404()

        project_invite.delete()
        return redirect("index")

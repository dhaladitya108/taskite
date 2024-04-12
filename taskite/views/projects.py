from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import Http404
from rest_framework import serializers

from taskite.models import Project, User, State


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "slug", "name", "description", "created_at"]


class ProjectCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "projects/create.html")


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

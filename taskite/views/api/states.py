from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from taskite.models import Project, State, Task, User
from taskite.mixins import ProjectFetchMixin
from taskite.permissions import ProjectMemberAPIPermission


class AssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "display_name", "email", "full_name", "created_at"]


class TaskSerializer(serializers.ModelSerializer):
    assignees = AssigneeSerializer(many=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "task_id",
            "name",
            "description",
            "priority",
            "order",
            "sequence",
            "created_at",
            "assignees",
        ]


class StateSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = ["id", "name", "order", "color", "tasks", "created_at"]

    def get_tasks(self, obj):
        return TaskSerializer(obj.state_tasks, many=True).data


class StateListCreateAPIView(ProjectFetchMixin, APIView):
    permission_classes = [IsAuthenticated, ProjectMemberAPIPermission]

    def get(self, request, *args, **kwargs):
        project = request.project
        task_queryset = Task.objects.order_by("order").prefetch_related("assignees")
        priorities = request.query_params.getlist("priorities[]")
        assignees = request.query_params.getlist("assignees[]")
        if len(priorities) > 0:
            task_queryset = task_queryset.filter(priority__in=priorities)

        if len(assignees) > 0:
            task_queryset = task_queryset.filter(task_assignees__user__in=assignees)

        states = (
            State.objects.filter(project=project)
            .prefetch_related(
                Prefetch(
                    "state_tasks",
                    queryset=task_queryset,
                )
            )
            .order_by("order")
        )
        return Response(
            data=StateSerializer(states, many=True).data, status=status.HTTP_200_OK
        )


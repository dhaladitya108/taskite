from django.db import transaction
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from taskite.models import Task, Project, State
from taskite.permissions import ProjectMemberAPIPermission
from taskite.mixins import ProjectFetchMixin
from taskite.exceptions import TaskNotFoundAPIException


class TaskUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    priority = serializers.ChoiceField(choices=Task.Priority.choices, required=False)
    order = serializers.FloatField(required=False)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "priority",
            "order",
            "sequence",
            "created_at",
        ]


class TaskListCreateAPIView(APIView):
    def get(self, request, project_id):
        return Response(data={}, status=status.HTTP_200_OK)


class TaskDetailUpdateDestroyAPIView(ProjectFetchMixin, APIView):
    permission_classes = [IsAuthenticated, ProjectMemberAPIPermission]

    def patch(self, request, *args, **kwargs):
        task = Task.objects.filter(
            project=request.project, id=kwargs.get("task_id")
        ).first()
        if not task:
            raise TaskNotFoundAPIException

        serializer = TaskUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={
                    "detail": "Invalid details provided for updating the given task."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = serializer.validated_data
        for attr, value in data.items():
            setattr(task, attr, value)
        task.save(update_fields=data.keys())

        state_id = request.query_params.get("state_id", None)
        if state_id:
            state = State.objects.filter(project=request.project, id=state_id).first()
            task.state = state
            task.save(update_fields=["state"])

        index = request.query_params.get("index", None)
        if index:
            task.update_order(index=int(index))

        return Response(
            data={"detail": "Task has been updated"}, status=status.HTTP_200_OK
        )

import time
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from taskite.models import Task, State, User
from taskite.permissions import ProjectMemberAPIPermission
from taskite.mixins import ProjectFetchMixin
from taskite.exceptions import (
    TaskNotFoundAPIException,
    StateNotFoundAPIException,
    InvalidRequestBodyAPIException,
)
from taskite.api.tasks.serializers import (
    TaskUpdateSerializer,
    TaskSerializer,
    TaskCreateSerializer,
    TaskDetailSerializer
)


class TaskListCreateAPIView(ProjectFetchMixin, APIView):
    permission_classes = [IsAuthenticated, ProjectMemberAPIPermission]

    def get(self, request, project_id):
        return Response(data={}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project = request.project

        serializer = TaskCreateSerializer(data=request.data)
        if not serializer.is_valid():
            raise InvalidRequestBodyAPIException

        data = serializer.validated_data

        state_id = data.get("state_id")
        state = State.objects.filter(project=project, id=state_id).first()
        if not state:
            return StateNotFoundAPIException

        task = Task(**data)
        task.state = state
        task.project = project
        task.save()

        return Response(
            data={
                "detail": "Task got created successfully.",
                "task": TaskSerializer(instance=task).data,
            },
            status=status.HTTP_201_CREATED,
        )


class TaskDetailUpdateDestroyAPIView(ProjectFetchMixin, APIView):
    permission_classes = [IsAuthenticated, ProjectMemberAPIPermission]

    def get(self, request, *args, **kwargs):
        # time.sleep(1)

        task = Task.objects.filter(
            project=request.project, id=kwargs.get("task_id")
        ).prefetch_related("assignees").prefetch_related("labels").first()
        if not task:
            raise TaskNotFoundAPIException
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)        


    def patch(self, request, *args, **kwargs):
        task = Task.objects.filter(
            project=request.project, id=kwargs.get("task_id")
        ).first()
        if not task:
            raise TaskNotFoundAPIException

        serializer = TaskUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            raise InvalidRequestBodyAPIException

        data = serializer.validated_data

        state_id = data.get("state_id", None)
        if state_id:
            if not State.objects.filter(project=request.project, id=state_id).exists():
                raise StateNotFoundAPIException
            
        assignee_ids = data.pop("assignee_ids", None)
        if assignee_ids:
            assignees = User.objects.filter(user_project__project=task.project, id__in=assignee_ids)
            task.assignees.set(assignees)

        for attr, value in data.items():
            setattr(task, attr, value)
        task.save(update_fields=data.keys())

        return Response(
            data={"detail": "Task has been updated", "task": TaskSerializer(task).data},
            status=status.HTTP_200_OK,
        )

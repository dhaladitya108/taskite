from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from taskite.models import Project, State, Task, User


class AssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "display_name", "email", "full_name", "created_at"]


class TaskSerializer(serializers.ModelSerializer):
    assignees = AssigneeSerializer(many=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "task_id",
            "name",
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


class StateListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, project_id):
        project = Project.objects.filter(id=project_id).first()
        if not project:
            return Response(
                data={"detail": "No project found with the given project id."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        states = (
            State.objects.filter(project=project)
            .prefetch_related(
                Prefetch(
                    "state_tasks",
                    queryset=Task.objects.order_by("order").prefetch_related(
                        "assignees"
                    ),
                )
            )
            .order_by("order")
        )
        return Response(
            data=StateSerializer(states, many=True).data, status=status.HTTP_200_OK
        )


class StateTaskListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, project_id, pk):
        project = Project.objects.filter(id=project_id).first()
        if not project:
            return Response(
                data={"detail": "No project found with the given project id."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        state = State.objects.filter(project=project, id=pk).first()
        if not state:
            return Response(
                data={"detail": "No state found with the given state id."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        tasks = (
            Task.objects.filter(project=project, state=state)
            .order_by("order")
            .prefetch_related("state_tasks")
        )
        return Response(
            data=TaskSerializer(tasks, many=True).data, status=status.HTTP_200_OK
        )

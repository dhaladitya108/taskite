from rest_framework import serializers

from taskite.models import Task, User, Label


class TaskUpdateSerializer(serializers.Serializer):
    state_id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    priority = serializers.ChoiceField(choices=Task.Priority.choices, required=False)
    order = serializers.FloatField(required=False)
    task_type = serializers.ChoiceField(choices=Task.TaskType.choices, required=False)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "task_id",
            "name",
            "task_type",
            "description",
            "priority",
            "order",
            "sequence",
            "created_at",
        ]


class TaskCreateSerializer(serializers.Serializer):
    state_id = serializers.UUIDField()
    name = serializers.CharField()
    priority = serializers.CharField(required=False)
    order = serializers.FloatField(required=False)
    description = serializers.CharField(required=False)
    task_type = serializers.CharField(required=False)


class TaskAssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "full_name",
            "display_name",
            "created_at"
        ]


class TaskLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = [
            "id",
            "name",
            "color",
            "created_at"
        ]


class TaskDetailSerializer(serializers.ModelSerializer):
    assignees = TaskAssigneeSerializer(many=True)
    labels = TaskLabelSerializer(many=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "task_id",
            "task_type",
            "name",
            "description",
            "priority",
            "start_date",
            "target_date",
            "order",
            "sequence",
            "assignees",
            "labels",
            "created_at"
        ]
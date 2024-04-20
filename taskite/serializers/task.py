from rest_framework import serializers

from taskite.models import Task


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

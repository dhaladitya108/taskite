from rest_framework import serializers

from taskite.models import Project, User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "slug", "visibility", "created_at"]


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "full_name", "display_name", "created_at"]


class ProjectCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    visibility = serializers.ChoiceField(choices=Project.Visibility.choices)
    description = serializers.CharField(required=False, allow_blank=True)
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
    identifier = serializers.SlugField(required=False)
    visibility = serializers.CharField()
    description = serializers.CharField(required=False)
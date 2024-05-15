from rest_framework import serializers

from taskite.models import Project, User, ProjectMember


class ProjectSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(use_url=False)
    cover_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "project_id",
            "description",
            "slug",
            "cover",
            "cover_url",
            "theme_color",
            "visibility",
            "created_at",
        ]

    def get_cover_url(self, obj):
        if not obj.cover:
            return None

        return obj.cover.url


class ProjectUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    slug = serializers.CharField(required=False)
    project_id = serializers.CharField(required=False)
    visibility = serializers.ChoiceField(
        choices=Project.Visibility.choices, required=False
    )
    cover = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    theme_color = serializers.CharField(required=False)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "full_name",
            "display_name",
            "avatar",
            "created_at",
        ]


class ProjectCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    visibility = serializers.ChoiceField(choices=Project.Visibility.choices)
    description = serializers.CharField(required=False, allow_blank=True)


class ProjectMemberSerializer(serializers.ModelSerializer):
    user = MemberSerializer()

    class Meta:
        model = ProjectMember
        fields = ["id", "user", "role", "created_at"]


class ProjectMemberUpdateSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=ProjectMember.Role.choices)


class ProjectMemberInviteSerializer(serializers.Serializer):
    emails = serializers.ListField()
    role = serializers.ChoiceField(choices=ProjectMember.Role.choices)
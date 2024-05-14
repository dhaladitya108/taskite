from rest_framework import serializers

from taskite.models import Project, User


class ProjectSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(use_url=False)
    cover_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "slug",
            "name",
            "description",
            "cover",
            "cover_url",
            "theme_color",
            "visibility",
            "project_id",
            "created_at",
        ]

    
    def get_cover_url(self, obj):
        if not obj.cover:
            return None
        
        return obj.cover.url



class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(use_url=False)
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "full_name",
            "display_name",
            "email",
            "avatar",
            "avatar_url",
            "created_at"
        ]

    def get_avatar_url(self, obj):
        if not obj.avatar:
            return None
        
        return obj.avatar.url
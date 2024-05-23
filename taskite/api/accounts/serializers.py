from rest_framework import serializers

from taskite.models import User


class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ProfileUpdateSerializer(serializers.Serializer):
    avatar = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    full_name = serializers.CharField(required=False)
    display_name = serializers.CharField(required=False)


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
            "created_at",
        ]

    def get_avatar_url(self, obj):
        if not obj.avatar:
            return None

        return obj.avatar.url

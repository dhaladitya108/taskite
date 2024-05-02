from rest_framework import serializers

from taskite.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "full_name",
            "display_name",
            "role",
            "is_active",
            "created_at"
        ]
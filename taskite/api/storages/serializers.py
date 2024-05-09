from rest_framework import serializers


class StoragePresignedSerializer(serializers.Serializer):
    filename = serializers.CharField()
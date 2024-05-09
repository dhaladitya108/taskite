
import boto3
from botocore.config import Config
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from taskite.api.storages.serializers import StoragePresignedSerializer
from taskite.exceptions import InvalidRequestBodyAPIException
from taskite.models import Storage

s3_config = Config(
    region_name = settings.AWS_REGION,
    signature_version = 'v4',
    # retries = {
    #     'max_attempts': 10,
    #     'mode': 'standard'
    # }
)


class StoragePresignedURLAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = StoragePresignedSerializer(data=request.data)
        
        if not serializer.is_valid():
            raise InvalidRequestBodyAPIException

        data = serializer.validated_data
        upload_key = Storage.get_upload_path(filename=data.get("filename"))

        client = boto3.client(
            "s3",
            endpoint_url=settings.AWS_ENDPOINT,
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY,
            config=s3_config,
        )
        res = client.generate_presigned_post(settings.AWS_BUCKET_NAME, upload_key)
        res_data = {
            "url": res["url"],
            "resource_url": f"{res["url"]}/{res["fields"]["key"]}",
            "resource_name": res["fields"]["key"],
            "fields": res["fields"]
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

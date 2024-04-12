from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class TaskListCreateAPIView(APIView):
    def get(self, request, project_id):
        return Response(data={}, status=status.HTTP_200_OK)
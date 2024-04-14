from django.contrib.auth import login
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView

from taskite.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={
                    "detail": "Invalid information provided.",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = serializer.validated_data
        password = data.pop("password")

        user = User.objects.filter(email=data.get("email")).first()
        if not user:
            return Response(
                data={
                    "detail": "Either the email or password entered is incorrect.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if not user.check_password(password):
            return Response(
                data={
                    "detail": "Either the email or password entered is incorrect.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        login(request, user)
        return Response(data={"detail": "Login success"}, status=status.HTTP_200_OK)

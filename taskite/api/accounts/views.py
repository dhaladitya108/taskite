from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from taskite.models import User, Storage
from taskite.api.accounts.serializers import (
    LoginSerializer,
    ProfileUpdateSerializer,
    ProfileSerializer,
    RegisterSerializer,
)
from taskite.exceptions import InvalidRequestBodyAPIException


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
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
        if User.objects.filter(email=data.get("email")).exists():
            return Response(
                data={"detail": "A user already exists with the given email address!"},
                status=status.HTTP_403_FORBIDDEN,
            )
        user = User(**data)
        user.set_password(password)
        user.save()
        login(request, user)
        return Response(data={"detail": "Register success"}, status=status.HTTP_200_OK)


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


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        serializer = ProfileUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            raise InvalidRequestBodyAPIException

        data = serializer.validated_data
        for attr, value in data.items():
            prev_value = getattr(user, attr)
            setattr(user, attr, value)
            new_value = getattr(user, attr)

            # Handling File Updates
            if attr == "avatar" and prev_value != new_value:
                if prev_value:
                    Storage.delete_upload(prev_value)
                if new_value:
                    Storage.confirm_upload(new_value)

        user.save(update_fields=data.keys())
        response_data = {
            "detail": "Profile got updated.",
            "profile": ProfileSerializer(user).data,
        }
        return Response(data=response_data, status=status.HTTP_200_OK)

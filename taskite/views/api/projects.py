from django.db import transaction
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from taskite.models import Project, ProjectMember, User
from taskite.permissions import ProjectMemberAPIPermission
from taskite.mixins import ProjectFetchMixin


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "slug", "visibility", "created_at", "updated_at"]


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "full_name", "display_name", "created_at"]


class ProjectCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    identifier = serializers.SlugField(required=False)
    visibility = serializers.CharField()
    description = serializers.CharField(required=False)


class ProjectListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == "admin":
            projects = Project.objects.all()
        else:
            user_projects = Project.objects.filter(project_member__user=request.user)
            public_projects = Project.objects.filter(
                visibility=Project.Visibility.PUBLIC
            )
            projects = user_projects.union(public_projects, all=False)

        serializer = ProjectSerializer(projects, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={"detail": "Invalid projected information provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_project_data = serializer.validated_data
        with transaction.atomic():
            project: Project = Project.objects.create(
                **new_project_data, created_by=request.user
            )
            if project.visibility == Project.Visibility.PUBLIC:
                ProjectMember.objects.create(
                    project=project, user=request.user, role=ProjectMember.Role.ADMIN
                )

        return Response(
            data={
                "detail": "Project has been created successfully.",
                "project": ProjectSerializer(project).data,
            },
            status=status.HTTP_200_OK,
        )


class ProjectMemberListAPIView(ProjectFetchMixin, APIView):
    permission_classes = [IsAuthenticated, ProjectMemberAPIPermission]

    def get(self, request, *args, **kwargs):
        project = request.project
        members = project.members.all().order_by("full_name")
        return Response(
            data=MemberSerializer(members, many=True).data, status=status.HTTP_200_OK
        )

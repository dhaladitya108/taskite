from django.db import transaction
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from taskite.models import Project, ProjectMember, User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "slug", "visibility", "created_at", "updated_at"]


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "full_name"]


class ProjectCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    identifier = serializers.SlugField(required=False)
    visibility = serializers.CharField()
    description = serializers.CharField(required=False)


class ProjectListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_projects = Project.objects.filter(project_member__user=request.user)
        public_projects = Project.objects.filter(visibility=Project.Visibility.PUBLIC)
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


class ProjectMemberListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        project = Project.objects.filter(id=pk).first()
        if not project:
            return Response(
                data={"detail": "No project found with the given project id."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        members = project.members.all()
        return Response(
            data=MemberSerializer(members, many=True).data, status=status.HTTP_200_OK
        )

from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from taskite.models import Project, ProjectMember
from taskite.permissions import ProjectMemberAPIPermission
from taskite.mixins import ProjectFetchMixin
from taskite.api.projects.serializers import (
    ProjectSerializer,
    MemberSerializer,
    ProjectCreateSerializer,
    ProjectMemberSerializer,
    ProjectMemberUpdateSerializer,
)
from taskite.exceptions import (
    ProjectMemberNotFoundAPIException,
    InvalidRequestBodyAPIException,
)


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
            print(serializer.errors)

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


class ProjectMembersAPIView(ProjectFetchMixin, APIView):
    permission_classes = [IsAuthenticated, ProjectMemberAPIPermission]

    def get(self, request, *args, **kwargs):
        project = request.project
        members = project.members.all().order_by("full_name")
        return Response(
            data=MemberSerializer(members, many=True).data, status=status.HTTP_200_OK
        )


class ProjectMembersListAPIView(ProjectFetchMixin, APIView):
    permission_classes = [IsAuthenticated, ProjectMemberAPIPermission]

    def get(self, request, *args, **kwargs):
        project = request.project
        project_members = ProjectMember.objects.filter(project=project).select_related(
            "user"
        )
        serializer = ProjectMemberSerializer(project_members, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProjectMemberRetrieveUpdateDestroyAPIView(ProjectFetchMixin, APIView):
    permission_classes = [IsAuthenticated, ProjectMemberAPIPermission]

    def patch(self, request, *args, **kwargs):
        project = request.project
        project_member = ProjectMember.objects.filter(
            project=project, id=kwargs.get("project_member_id")
        ).first()
        if not project_member:
            raise ProjectMemberNotFoundAPIException

        serializer = ProjectMemberUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            raise InvalidRequestBodyAPIException

        data = serializer.validated_data
        for attr, value in data.items():
            setattr(project_member, attr, value)
        project_member.save(update_fields=data.keys())

        project_member_serializer = ProjectMemberSerializer(project_member)
        return Response(data=project_member_serializer.data, status=status.HTTP_200_OK)

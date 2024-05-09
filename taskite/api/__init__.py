from django.urls import path

from taskite.api.home.views import LoginAPIView, ProfileAPIView
from taskite.api.projects.views import (
    ProjectListCreateAPIView,
    ProjectMembersAPIView,
    ProjectMembersListAPIView,
    ProjectMemberRetrieveUpdateDestroyAPIView,
    ProjectDetailUpdateDestroyAPIView
)
from taskite.api.states.views import StateListCreateAPIView
from taskite.api.tasks.views import (
    TaskListCreateAPIView,
    TaskDetailUpdateDestroyAPIView,
)
from taskite.api.labels.views import LabelListCreateAPIView
from taskite.api.users.views import UserListAPIView
from taskite.api.storages.views import StoragePresignedURLAPIView

# fmt: off
urlpatterns = [
    path("storages/presigned-url/", StoragePresignedURLAPIView.as_view()),
    path("home/login/", LoginAPIView.as_view()),
    path("home/profile/", ProfileAPIView.as_view()),
    path("users/", UserListAPIView.as_view()),
    path("projects/", ProjectListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/", ProjectDetailUpdateDestroyAPIView.as_view()),
    path("projects/<uuid:project_id>/members/", ProjectMembersAPIView.as_view()),
    path("projects/<uuid:project_id>/project_members/", ProjectMembersListAPIView.as_view()),
    path("projects/<uuid:project_id>/project_members/<uuid:project_member_id>/", ProjectMemberRetrieveUpdateDestroyAPIView.as_view()),
    path("projects/<uuid:project_id>/states/", StateListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/tasks/", TaskListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/tasks/<uuid:task_id>/", TaskDetailUpdateDestroyAPIView.as_view()),
    path("projects/<uuid:project_id>/labels/", LabelListCreateAPIView.as_view()),
]

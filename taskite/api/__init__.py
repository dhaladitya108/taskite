from django.urls import path

from taskite.api.home.views import LoginAPIView
from taskite.api.projects.views import (
    ProjectListCreateAPIView,
    ProjectMemberListAPIView,
)
from taskite.api.states.views import StateListCreateAPIView
from taskite.api.tasks.views import (
    TaskListCreateAPIView,
    TaskDetailUpdateDestroyAPIView,
)
from taskite.api.labels.views import LabelListCreateAPIView

# fmt: off
urlpatterns = [
    path("home/login/", LoginAPIView.as_view()),
    path("projects/", ProjectListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/members/", ProjectMemberListAPIView.as_view()),
    path("projects/<uuid:project_id>/states/", StateListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/tasks/", TaskListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/tasks/<uuid:task_id>/", TaskDetailUpdateDestroyAPIView.as_view()),
    path("projects/<uuid:project_id>/labels/", LabelListCreateAPIView.as_view()),
]
from django.urls import path

from taskite.views.api.home import LoginAPIView
from taskite.views.api.projects import (
    ProjectListCreateAPIView,
    ProjectMemberListAPIView,
)
from taskite.views.api.states import StateListCreateAPIView
from taskite.views.api.tasks import (
    TaskListCreateAPIView,
    TaskDetailUpdateDestroyAPIView,
)
from taskite.views.api.labels import LabelListCreateAPIView

# fmt: off
urlpatterns = [
    path("home/login/", LoginAPIView.as_view()),
    path("projects/", ProjectListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/labels/", LabelListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/members/", ProjectMemberListAPIView.as_view()),
    path("projects/<uuid:project_id>/states/", StateListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/tasks/", TaskListCreateAPIView.as_view()),
    path("projects/<uuid:project_id>/tasks/<uuid:task_id>/", TaskDetailUpdateDestroyAPIView.as_view()),
]

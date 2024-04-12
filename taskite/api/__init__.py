from django.urls import path

from taskite.api.home import LoginAPIView
from taskite.api.project import ProjectListCreateAPIView, ProjectMemberListAPIView
from taskite.api.task import TaskListCreateAPIView
from taskite.api.state import StateListCreateAPIView, StateTaskListCreateAPIView

urlpatterns = [
    path("home/login/", LoginAPIView.as_view()),
    path("projects/", ProjectListCreateAPIView.as_view()),
    path("projects/<int:pk>/members/", ProjectMemberListAPIView.as_view()),
    path("projects/<int:project_id>/states/", StateListCreateAPIView.as_view()),
    path("projects/<int:project_id>/states/<int:pk>/tasks/", StateTaskListCreateAPIView.as_view()),
    path("projects/<project_id>/tasks/", TaskListCreateAPIView.as_view())
]
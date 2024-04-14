from django.urls import path

from taskite.views.api.home import LoginAPIView
from taskite.views.api.projects import ProjectListCreateAPIView, ProjectMemberListAPIView
from taskite.views.api.states import StateListCreateAPIView
from taskite.views.api.tasks import TaskListCreateAPIView, TaskDetailUpdateDestroyAPIView


urlpatterns = [
    path("home/login/", LoginAPIView.as_view()),
    path("projects/", ProjectListCreateAPIView.as_view()),
    path("projects/<int:project_id>/members/", ProjectMemberListAPIView.as_view()),
    path("projects/<int:project_id>/states/", StateListCreateAPIView.as_view()),
    path("projects/<int:project_id>/tasks/", TaskListCreateAPIView.as_view()),
    path("projects/<int:project_id>/tasks/<int:task_id>/", TaskDetailUpdateDestroyAPIView.as_view())
]
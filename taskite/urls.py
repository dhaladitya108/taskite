from django.contrib import admin
from django.urls import path, include

from taskite.views.home import LoginView, IndexView, LogoutView
from taskite.views.projects import ProjectDetailView, ProjectTaskView
from taskite.views.settings import MembersView

# fmt: off
urlpatterns = [
    # Public API Endpoints
    path("api/v1/", include("taskite.api.v1")),

    # Internal API Endpoints
    path("api/", include("taskite.api")),

    # Admin routes
    path("admin/", admin.site.urls),

    # Other routes
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("settings/members/", MembersView.as_view(), name="members"),
    path("<str:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("<str:slug>/<str:task_id>/", ProjectTaskView.as_view(), name="project-task"),
    path("", IndexView.as_view(), name="index")
]

from django.contrib import admin
from django.urls import path, include

from taskite.views.home import LoginView, IndexView, LogoutView
from taskite.views.projects import ProjectDetailView, ProjectCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("taskite.views.api")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create/", ProjectCreateView.as_view(), name="project-create"),
    path("<str:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("", IndexView.as_view(), name="index")
]

from django.contrib import admin
from django.urls import path, include

from taskite.views.home import LoginView, IndexView, LogoutView
from taskite.views.projects import ProjectDetailView

urlpatterns = [
    # Public API Endpoints
    path("api/v1/", include("taskite.views.api.v1")),
    path("api/v2/", include("taskite.views.api.v2")),

    # Internal API Endpoints
    path("api/", include("taskite.views.api")),

    # Admin routes
    path("admin/", admin.site.urls),

    # Other routes
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<str:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("", IndexView.as_view(), name="index")
]

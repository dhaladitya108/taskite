from django.contrib import admin
from django.urls import path, include

from taskite.views.home import LoginView, IndexView, LogoutView
from taskite.views.projects import ProjectDetailView, ProjectTaskView, ProjectSettingsMembersView, ProjectSettingsGeneralView
from taskite.views.settings import UsersView, ProfileView

# fmt: off
urlpatterns = [
    # Internal API Endpoints
    path("api/", include("taskite.api")),

    # Admin routes
    path("admin/", admin.site.urls),

    # Other routes
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("settings/users/", UsersView.as_view(), name="settings-users"),
    path("settings/profile/", ProfileView.as_view(), name="settings-profile"),
    path("<str:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("<str:slug>/settings/general/", ProjectSettingsGeneralView.as_view(), name="project-settings-general"),
    path("<str:slug>/settings/members/", ProjectSettingsMembersView.as_view(), name="project-settings-members"),
    path("<str:slug>/<str:task_id>/", ProjectTaskView.as_view(), name="project-task"),
    path("", IndexView.as_view(), name="index")
]

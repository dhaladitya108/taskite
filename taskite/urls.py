from django.contrib import admin
from django.urls import path, include

from taskite.views.home import LoginView, IndexView, LogoutView
from taskite.views.projects import (
    ProjectDetailView,
    ProjectTaskView,
    ProjectSettingsGeneralView,
    ProjectListView,
    ProjectSettingsMembersView,
    ProjectInviteConfirmationView,
    ProjectInviteRejectionView
)
from taskite.views.settings import ProfileView

# fmt: off
urlpatterns = [
    # Internal API Endpoints
    path("api/", include("taskite.api")),

    # Admin routes
    path("admin/", admin.site.urls),

    # Other routes
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("settings/profile/", ProfileView.as_view(), name="settings-profile"),
    path("projects/invite/<uuid:project_invite_id>/confirm/", ProjectInviteConfirmationView.as_view(), name="project-invite-confirm"),
    path("projects/invite/<uuid:project_invite_id>/reject/", ProjectInviteRejectionView.as_view(), name="project-invite-reject"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("<str:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("<str:slug>/settings/general/", ProjectSettingsGeneralView.as_view(), name="project-settings-general"),
    path("<str:slug>/settings/members/", ProjectSettingsMembersView.as_view(), name="project-settings-members"),
    path("<str:slug>/<str:task_id>/", ProjectTaskView.as_view(), name="project-task"),
    path("", IndexView.as_view(), name="index")
]

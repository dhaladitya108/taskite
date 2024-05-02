from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "settings/profile.html")


class UsersView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "settings/users.html")

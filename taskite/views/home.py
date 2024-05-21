import humps
from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from taskite.serializers import ProfileSerializer


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        serializer = ProfileSerializer(user)
        context = {"props": {"user": humps.camelize(serializer.data)}}
        return render(request, "home/index.html", context)


class LoginView(View):
    def get(self, request):
        context = {"props": {"next": request.GET.get("next", "/")}}
        return render(request, "home/login.html", context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

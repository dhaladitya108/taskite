import humps
from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):
    def get(self, request):
        context = {"props": {"next": request.GET.get("next", "/")}}
        return render(request, "accounts/login.html", context)


class RegisterView(View):
    def get(self, request):
        return render(request, "accounts/register.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

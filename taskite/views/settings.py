import humps
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from taskite.serializers import ProfileSerializer


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        serializer = ProfileSerializer(user)
        context = {
            "props": {
                "profile": humps.camelize(serializer.data)
            }
        }
        return render(request, "settings/profile.html", context)

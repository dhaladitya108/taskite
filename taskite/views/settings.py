from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render



class MembersView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "settings/members.html")
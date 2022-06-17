from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.conf import settings
from .models import Place


class MemoryCreationView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        context = {"key": settings.GOOGLE_API_KEY}
        return render(request, "memory/creation.html", context=context)

    def post(self, request: HttpRequest):
        place = Place()
        place.name = request.POST.get("name")
        place.comment = request.POST.get("comment")
        place.latitude = request.POST.get("lat")
        place.longitude = request.POST.get("lng")
        place.user = request.user
        place.save()

        return redirect("home")

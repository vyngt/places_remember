from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import redirect


class Home(TemplateView):
    template_name = "home.html"


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("home")

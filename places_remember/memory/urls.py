from django.urls import path
from .views import MemoryCreationView

app_name = "memory"

urlpatterns = [
    path("", MemoryCreationView.as_view(), name="creation"),
]

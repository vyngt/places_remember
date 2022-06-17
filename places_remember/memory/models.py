from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=200, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-created"]

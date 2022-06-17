from django.test import TestCase
from django.contrib.auth.models import User
from .models import Place


class PlaceTestCase(TestCase):
    def setUp(self):
        user01 = User.objects.create(username="user01")
        Place.objects.create(
            name="Hanoi",
            longitude="105.85434502297329",
            latitude="20.9444799049412",
            user=user01,
        )
        Place.objects.create(
            name="Ho Chi Minh",
            longitude="106.63290448811489",
            latitude="10.740037995214262",
            user=user01,
        )
        user02 = User.objects.create(username="user02")
        Place.objects.create(
            name="Tokyo",
            longitude="139.7733826581909",
            latitude="35.65092532751842",
            user=user02,
        )
        Place.objects.create(
            name="Da Lat",
            longitude="108.47508703872852",
            latitude="11.854491296995105",
            user=user02,
        )

    def test_user01_memories(self):
        user01 = User.objects.get(username="user01")
        memories_u1 = [memory.name for memory in user01.place_set.order_by("-pk")]
        self.assertEqual(memories_u1, ["Ho Chi Minh", "Hanoi"])

    def test_user02_memories(self):
        user02 = User.objects.get(username="user02")
        memories_u2 = [memory.name for memory in user02.place_set.order_by("-pk")]
        self.assertEqual(memories_u2, ["Da Lat", "Tokyo"])

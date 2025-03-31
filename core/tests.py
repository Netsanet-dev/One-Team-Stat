from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import MyUser
from .views import register_user
from .serializers import UserRegistrationSerializer

# Create your tests here.
class RegisterViewTest(APITestCase):

    def setup(self):
        self.user = MyUser.objects.create(name="netsanet", password="1234567")

    def test_register (self):
        url = reverse('register')
        response = self.client.get(url, format='json')
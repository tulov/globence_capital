from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):
    def setUp(self) -> None:
        User.objects.create(username='lex',
                            first_name='Alexey',
                            last_name='Tulovskiy',
                            email='tulov.alex@gmail.com',
                            is_superuser=True,
                            is_active=True,
                            password='123456')

    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.json()
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]['username'], 'lex')

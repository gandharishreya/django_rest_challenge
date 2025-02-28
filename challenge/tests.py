from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.test import APIClient

class UserGroupAPITest(TestCase):

    def setUp(self):
        # Create a test user and group
        self.user = User.objects.create_user(username='testuser', password='password')
        self.group = Group.objects.create(name='testgroup')
        self.client = APIClient()

        # Authenticate the user
        self.client.login(username='testuser', password='password')

    def test_create_user(self):
        """Test creating a user"""
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post('/users/', data, format='json')  # Assuming users URL
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')

    def test_create_group(self):
        """Test creating a group"""
        data = {'name': 'newgroup'}
        response = self.client.post('/groups/', data, format='json')  # Assuming groups URL
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'newgroup')

    def test_user_permission(self):
        """Test that authentication is required for accessing users"""
        self.client.logout()
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_group_permission(self):
        """Test that authentication is required for accessing groups"""
        self.client.logout()
        response = self.client.get('/groups/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
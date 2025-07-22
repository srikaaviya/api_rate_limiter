from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class RateLimitTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_rate_limit(self):
        url = '/api/protected/'
        for _ in range(5):
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

        # 6th request should fail
        response = self.client.get(url)
        self.assertEqual(response.status_code, 429)

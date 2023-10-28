from django.test import TestCase
from rest_framework.test import APITestCase

from django.urls import reverse

from books import models as books_models

# Create your tests here.

class TestBookApi(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = books_models.Book.objects.create(
            title='some title',
            subtitle='some subtiel',
            author='some author',
            isbn='some isbn'
        )

    def test_api(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(books_models.Book.objects.count(), 1)
        

    

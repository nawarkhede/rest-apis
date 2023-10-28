from django.test import TestCase
from . import models as books_models
from django.urls import reverse

# Create your tests here.

class TestBook(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = books_models.Book.objects.create(
            title='some title',
            subtitle='some subtiel',
            author='some author',
            isbn='some isbn'
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "some title")
        self.assertEqual(self.book.subtitle, "some subtiel")
        self.assertEqual(self.book.author, "some author")
        self.assertEqual(self.book.isbn, "some isbn")

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "some title")
        self.assertTemplateUsed(response, "books/book_list.html")
import json

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Book


class FillDatabaseTest(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            id="FFnSBgAAQBAJ",
            title="Test title",
            authors=["Test author 1", "Test author 2"],
            categories=[],
            average_rating=0,
            ratings_count=0,
            published_date="2016-05-05",
            thumbnail="thumbnail"
        )

    def test_fill_db_no_parameters(self):
        res = self.client.post(reverse("books:fill_db"))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data, "Wrong parameters")

    def test_fill_db_wrong_parameters(self):
        res = self.client.post(reverse("books:fill_db"), {"bad": "parameter"})
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data, "Wrong parameters")

        res = self.client.post(reverse("books:fill_db"), {"q": "bad"})
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data, "Wrong parameters")

    def test_fill_db_update_existing(self):
        res = self.client.post(reverse("books:fill_db"), {"q": "war"})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        book = self.client.get(reverse("books:retrieve_book", kwargs={"pk": "FFnSBgAAQBAJ"}))
        self.assertNotEqual(book.data["title"], self.book.title)

    def test_fill_db_success(self):
        res = self.client.post(reverse("books:fill_db"), {"q": "war"})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    class BooksListTest(APITestCase):
        def setUp(self):
            res = self.client.post(reverse("books:fill_db"), {"q": "war"})

        def test_books_list_success(self):
            res = self.client.get(reverse("books:books_list"))
            self.assertEqual(res.status_code, status.HTTP_200_OK)

    class RetrieveBookTest(APITestCase):
        def setUp(self):
            res = self.client.post(reverse("books:fill_db"), {"q": "war"})

        def _success(self):
            res = self.client.get(reverse("books:books_list"))
            self.assertEqual(res.status_code, status.HTTP_200_OK)

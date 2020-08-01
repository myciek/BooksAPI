import json

import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from .serializers import CreateBookSerializer, BookSerializer
from .models import Book
# Create your views here.
from rest_framework.views import APIView


class FillDatabaseAPIView(APIView):
    serializer_class = CreateBookSerializer

    def post(self, request):
        if "q" in request.data and request.data["q"] == "war":
            res = requests.get("https://www.googleapis.com/books/v1/volumes?q=war")
            data = json.loads(res.text)
            books = data["items"]
            for book in books:
                volume_info = book["volumeInfo"]
                book_data = {
                    "title": volume_info["title"],
                    "authors": volume_info["authors"],
                    "published_date": volume_info["publishedDate"],
                    "categories": volume_info.get("categories", []),
                    "average_rating": volume_info.get("averageRating", 0),
                    "ratings_count": volume_info.get("ratingsCount", 0),
                    "thumbnail": volume_info["imageLinks"]["thumbnail"]
                }
                try:
                    existing_book = Book.objects.get(id=book["id"])
                    serializer = self.serializer_class(existing_book, data=book_data, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                except Book.DoesNotExist:
                    book_data["id"] = book["id"]
                    serializer = self.serializer_class(data=book_data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
            books_list = Book.objects.all()
            serializer = self.serializer_class(books_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("Wrong parameters", status=status.HTTP_401_UNAUTHORIZED)


class ListBookAPIView(APIView):
    serializer_class = BookSerializer

    def get(self, request):
        books = Book.objects.all()
        serializer = self.serializer_class(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveBookAPIView(APIView):
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(id=self.kwargs["id"])
            serializer = self.serializer_class(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response("Book with this ID not found!", status=status.HTTP_401_UNAUTHORIZED)

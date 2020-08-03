import json

import requests
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .filters import BookFilter
from .parsers import book_parser
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
                book_data = book_parser(book)
                try:
                    existing_book = Book.objects.get(id=book["id"])
                    serializer = self.serializer_class(existing_book, data=book_data, partial=True)
                except Book.DoesNotExist:
                    book_data["id"] = book["id"]
                    serializer = self.serializer_class(data=book_data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            books_list = Book.objects.all()
            serializer = self.serializer_class(books_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("Wrong parameters", status=status.HTTP_401_UNAUTHORIZED)


class ListBookAPIView(ListAPIView):
    serializer_class = BookSerializer
    model = Book
    queryset = Book.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = BookFilter
    ordering_fields = ("published_date",)


class RetrieveBookAPIView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

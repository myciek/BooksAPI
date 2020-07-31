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
            return Response("Database filled.", status=status.HTTP_200_OK)
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

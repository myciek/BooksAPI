from rest_framework import serializers
from .models import Book


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id", "title", "authors", "published_date", "categories", "average_rating", "ratings_count", "thumbnail"
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
             "title", "authors", "published_date", "categories", "average_rating", "ratings_count", "thumbnail"
        )

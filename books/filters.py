from django_filters import filters, FilterSet

from books.models import Book


class BookFilter(FilterSet):
    authors = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ('authors', 'published_date')
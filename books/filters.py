from django_filters import filters, FilterSet

from books.models import Book


class BookFilter(FilterSet):
    author = filters.CharFilter(lookup_expr='icontains', field_name='authors')
    published_date = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ('author', 'published_date')
from django.urls import path
from .views import FillDatabaseAPIView, ListBookAPIView, RetrieveBookAPIView
app_name = 'books'

urlpatterns = [
    path('db', FillDatabaseAPIView.as_view(), name="fill_db"),
    path('books', ListBookAPIView.as_view(), name="books_list"),
    path('books/<pk>', RetrieveBookAPIView.as_view(), name="retrieve_book"),
    ]
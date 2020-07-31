from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Book(models.Model):
    title = models.TextField(max_length=255)
    authors = ArrayField(models.TextField(max_length=255))
    published_date = models.TextField(max_length=10)
    categories = ArrayField(models.TextField(max_length=255))
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    ratings_count = models.IntegerField(blank=True)
    thumbnail = models.TextField(max_length=1024)

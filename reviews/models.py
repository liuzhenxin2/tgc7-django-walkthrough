from django.db import models

# Create your models here.
from books.models import Book


class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    content = models.TextField(blank=False)
    date = models.DateField(blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review {self.title} for {self.book.title}"

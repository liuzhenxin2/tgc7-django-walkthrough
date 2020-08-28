from django.db import models

from books.models import Book
from django.contrib.auth.models import User

# Create your models here.


class Purchase(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Purchase made for id:{self.book.id} by {self.user.username}" \
            f" on {self.purchase_date}"

from django import forms
from .models import Book, Publisher, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'ISBN', 'desc', 'genre')


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'email')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

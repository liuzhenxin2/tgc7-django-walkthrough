from django import forms
from .models import Book, Publisher, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('owner',)


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'email')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

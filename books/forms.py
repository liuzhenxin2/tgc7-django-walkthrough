from django import forms
from .models import Book, Publisher, Author, Genre


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


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False)
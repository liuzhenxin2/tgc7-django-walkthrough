from django import forms
from .models import Book, Publisher, Author, Genre, Tag
from cloudinary.forms import CloudinaryJsFileField

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('owner',)
    cover = CloudinaryJsFileField()


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'email')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class SearchForm(forms.Form):
    search_terms = forms.CharField(max_length=100, required=False)
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required=False
    )

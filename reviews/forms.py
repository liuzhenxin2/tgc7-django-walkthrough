from django import forms

from .models import Review
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('book', 'author')


class SearchReviewForm(forms.Form):
    review_title = forms.CharField(required=False)
    book_title = forms.CharField(required=False)
    author = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

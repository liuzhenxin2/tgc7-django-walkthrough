from django import forms

from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('book', 'author')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('review', 'author')

from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, redirect
from .models import Review
from .forms import ReviewForm, CommentForm
from books.models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    all_reviews = Review.objects.all()
    return render(request, 'show_reviews.template.html', {
        'all_reviews': all_reviews
    })


@login_required
def create(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_model = form.save(commit=False)
            review_model.book = book
            review_model.author = request.user
            review_model.save()
            messages.success(request, "New review added successfully!")
            return redirect(reverse('book_details_route', kwargs={'book_id': book_id}))
    else:
        form = ReviewForm()
        return render(request, 'reviews/create.template.html', {
            'form': form,
            'book': book
        })


@login_required
def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        submitted_form = CommentForm(request.POST)
        if submitted_form.is_valid():
            # retrieve an instance of the Comment model without saving it
            # to the database because we need to do more processing
            new_comment = submitted_form.save(commit=False)
            # set the author of the comment to be the current logged in user
            new_comment.author = request.user
            # set the review that this comment belongs to
            new_comment.review = review
            # save the comment
            new_comment.save()
            return redirect(reverse('book_details_route',
                                    kwargs={'book_id': review.book.id}))
    else:
        comment_form = CommentForm()
        return render(request, 'reviews/create_comment.template.html', {
            'review': review,
            'form': comment_form
        })

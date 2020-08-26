from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, redirect
from .models import Review
from .forms import ReviewForm
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

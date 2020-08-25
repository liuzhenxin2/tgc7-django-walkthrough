from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Publisher, Author
from .forms import BookForm, PublisherForm, AuthorForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def welcome(request):
    return render(request, 'books/welcome.template.html')


def index(request):
    # create a query set that has all the books
    # a query set is like a cursor
    all_books = Book.objects.all()
    return render(request, "books/index.template.html", {
        'all_books': all_books
    })


def success(request):
    return render(request, 'books/login_success.template.html')


def show_publisher(request):
    all_publishers = Publisher.objects.all()
    return render(request, "books/show_publishers.template.html", {
        'all_publishers': all_publishers
    })


def show_authors(request):
    all_authors = Author.objects.all()
    return render(request, "books/show_authors.template.html", {
        'all_authors': all_authors
    })


@login_required
def create_book(request):
    # if the user submits the data
    if request.method == "POST":
        # take whatever the user has submitted (stored inside
        # request.POST) and populate an instance of BookForm
        submitted_form = BookForm(request.POST)

        # test if the form is valid
        if submitted_form.is_valid():
            submitted_form.save()
            messages.success(request, f"New book {submitted_form.title} has been created")
            return redirect(reverse(index))
    else:
        # if user did not submit the data, just display the form
        create_book_form = BookForm()
        return render(request, "books/create_book.template.html", {
            'form': create_book_form
        })


def create_publisher(request):
    if request.method == "POST":
        # 1. create the form and populate it with the user's input
        submitted_form = PublisherForm(request.POST)
        if submitted_form.is_valid():
            # 2. if the submitted information is valid, save
            submitted_form.save()
            return redirect(reverse(show_publisher))

    else:
        publisher_form = PublisherForm()
        return render(request, 'books/create_publisher.template.html', {
            'form': publisher_form
        })


def create_author(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect(reverse(show_authors))
    else:
        author_form = AuthorForm()
        return render(request, 'books/create_author.template.html', {
            'form': author_form
        })


def update_book(request, book_id):
    if request.method == "POST":
        # 1. retrieve the book that is being updated
        book_being_updated = get_object_or_404(Book, pk=book_id)

        # 2. do the modification
        book_form = BookForm(request.POST, instance=book_being_updated)

        # 3. save if the form is valid
        if book_form.is_valid():
            book_form.save()

            # 4. redirect
            return redirect(reverse(index))
    else:
        # 1. retrieve the book that we are editing
        book_being_updated = get_object_or_404(Book, pk=book_id)

        # 2. create the form containing the existing book's book data
        form = BookForm(instance=book_being_updated)

        # 3. display the form in a template
        return render(request, 'books/update_book.template.html', {
            'form': form
        })


# the second argument `book_id` is the id of the book
# that we want to delete
def delete_book(request, book_id):
    if request.method == "POST":
        book_to_delete = get_object_or_404(Book, pk=book_id)
        book_to_delete.delete()
        return redirect(reverse(index))
    else:
        # 1. fetch the book that we want to delete
        book_to_delete = get_object_or_404(Book, pk=book_id)

        # 2. ask for confirmation if we want to delete
        return render(request, 'books/delete_book.template.html', {
            'book': book_to_delete
        })

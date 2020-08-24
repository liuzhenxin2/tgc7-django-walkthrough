from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Publisher
from .forms import BookForm, PublisherForm
# Create your views here.


def welcome(request):
    return HttpResponse("welcome")


def index(request):
    # create a query set that has all the books
    # a query set is like a cursor
    all_books = Book.objects.all()
    return render(request, "books/index.template.html", {
        'all_books': all_books
    })


def show_publisher(request):
    all_publishers = Publisher.objects.all()
    return render(request, "books/show_publishers.template.html", {
        'all_publishers': all_publishers
    })


def create_book(request):
    # if the user submits the data
    if request.method == "POST":
        # take whatever the user has submitted (stored inside
        # request.POST) and populate an instance of BookForm
        submitted_form = BookForm(request.POST)

        # test if the form is valid
        if submitted_form.is_valid():
            submitted_form.save()
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

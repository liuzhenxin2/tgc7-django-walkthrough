from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from books.models import Book

# Create your views here.


def add_to_cart(request, book_id):
    # retrieve our shopping cart from the session
    # if there is no shopping cart, return an empty dictionary instead
    cart = request.session.get('shopping_cart', {})

    book = get_object_or_404(Book, pk=book_id)

    # if the book does not exists in the shopping cart
    if book_id not in cart:
        # add the book to the cart
        cart[book_id] = {
            'id': book_id,
            'title': book.title,
            'image': book.cover.url,
            'cost': f"{book.cost:.2f}",
            'qty': 1
        }
    else:
        # if the book already exists in the shopping cart
        cart[book_id]['qty'] += 1

    # re-save the shopping cart back into the session
    request.session['shopping_cart'] = cart

    messages.success(request,
                     f'Book {book.title} has been added to the shopping cart!')

    return redirect(reverse('view_all_books'))


def show_cart(request):
    cart = request.session.get('shopping_cart', {})
    total = 0
    for key, item in cart.items():
        total += float(item['cost'])

    return render(request, 'cart/view.template.html', {
        'cart': cart,
        'total': f"{total:.2f}"
    })


def remove_from_cart(request, book_id):
    cart = request.session.get('shopping_cart', {})

    if book_id in cart:
        # remove the book from the shopping cart
        del cart[book_id]

        # save back the cart
        request.session['shopping_cart'] = cart
        messages.success(
            request, "Item has been removed from the shopping cart")
    else:
        messages.success(request, "Item not found in shopping cart")

    return redirect(reverse('show_cart_route'))

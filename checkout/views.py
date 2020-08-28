from django.shortcuts import render, get_object_or_404, HttpResponse, reverse
from django.conf import settings
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

import stripe

from books.models import Book
from .models import Purchase

# Create your views here.


def checkout(request):

    # setup stripe
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrive the shopping cart
    cart = request.session.get('shopping_cart', {})

    # store all the line items in this list
    line_items = []
    all_book_ids = []

    # for each item in the shopping cart...
    for key, item in cart.items():

        book_model = get_object_or_404(Book, pk=item["id"])
        # create a line item
        item = {
            "name": book_model.title,
            # multiply the actual cost of the book to represent
            # the cost in cents and must be in integer
            "amount": int(book_model.cost * 100),
            "quantity": item["qty"],
            "currency": "usd"
        }

        line_items.append(item)
        all_book_ids.append(str(book_model.id))

    # get the domain name
    current_site = Site.objects.get_current()
    domain = current_site.domain

    # pass all the line items to stripe and in return
    # get a checkout session id
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        client_reference_id=request.user.id,
        mode='payment',
        success_url=domain + reverse('checkout_success_route'),
        cancel_url=domain + reverse('checkout_cancelled_route'),
        metadata={
            "all_book_ids": ",".join(all_book_ids)
        }
    )

    # render the template which will redirect to stripe
    return render(request, 'checkout/checkout.template.html', {
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    # empty the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Payment is successful")


def checkout_cancelled(request):
    return HttpResponse("Payment cancelled")


@csrf_exempt
def payment_completed(request):
    # payload represents the data sent back to us by Stripe
    payload = request.body
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(e)
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_payment(session)

    return HttpResponse(status=200)


def handle_payment(session):
    user = get_object_or_404(User, pk=session["client_reference_id"])

    all_book_ids = session['metadata']['all_book_ids'].split(',')
    for book_id in all_book_ids:
        book_model = get_object_or_404(Book, pk=book_id)

        # create a Purchase model manually
        purchase = Purchase()
        purchase.book = book_model
        purchase.user = user
        purchase.save()

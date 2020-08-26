from django.shortcuts import render, HttpResponse
from .models import Review
# Create your views here.


def index(request):
    all_reviews = Review.objects.all()
    return render(request, 'show_reviews.template.html', {
        'all_reviews': all_reviews
    })


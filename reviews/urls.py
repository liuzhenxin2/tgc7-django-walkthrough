from django.urls import path
import reviews.views

urlpatterns = [
    path('', reviews.views.index, name="view_reviews_route"),
    path('create/<book_id>', reviews.views.create, name="create_review_route")
]
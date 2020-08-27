from django.urls import path
import reviews.views

urlpatterns = [
    path('', reviews.views.index, name="view_reviews_route"),
    path('create/<book_id>', reviews.views.create, name="create_review_route"),
    path('review/<review_id>/comments/create', reviews.views.create_comment,
         name='create_comment_route')
]

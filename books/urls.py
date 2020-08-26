from django.urls import path
import books.views


urlpatterns = [
    path('', books.views.index),
    path('publishers/', books.views.show_publisher),
    path('create/', books.views.create_book),
    path('publishers/create', books.views.create_publisher),
    path('update/<book_id>', books.views.update_book,
         name="update_book_route"),
    path('authors/create', books.views.create_author),
    path('authors/', books.views.show_authors),
    path('delete/<book_id>', books.views.delete_book,
         name="delete_book_route"),
    path('details/<book_id>', books.views.view_book_details,
         name='book_details_route')
]

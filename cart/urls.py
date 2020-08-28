from django.urls import path
import cart.views

urlpatterns = [
    path('add/book/<book_id>', cart.views.add_to_cart,
         name="add_to_cart_route"),
    path('', cart.views.show_cart, name="show_cart_route"),
    path('remove/book/<book_id>', cart.views.remove_from_cart,
         name="remove_from_cart_route"),
    path('update/quantity/book/<book_id>', cart.views.update_quantity,
         name='update_cart_quantity')
]

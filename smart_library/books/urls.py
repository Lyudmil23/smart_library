from django.urls import path, include

from smart_library.books.views import BooksView, BookDetailsView, rent_book, RentedBooksView

urlpatterns = [
    path('', BooksView.as_view(), name='books'),
    path('book/<int:pk>/', include([
        path('', BookDetailsView.as_view(), name='book details'),
        path('rent/', rent_book, name='rent book'),
    ])),
    path('rented_books/', RentedBooksView.as_view(), name='rented books'),

]
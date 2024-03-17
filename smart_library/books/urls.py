from django.urls import path

from smart_library.books.views import BooksView

urlpatterns = [
    path('', BooksView.as_view(), name='books'),

]
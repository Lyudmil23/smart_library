from django.shortcuts import render
from django.views.generic import ListView

from smart_library.books.models import Book


class BooksView(ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'
    paginate_by = 6

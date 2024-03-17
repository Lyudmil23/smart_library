from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

from smart_library.books.models import Book


class BooksView(ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'
    paginate_by = 6


class BookDetailsView(TemplateView):
    template_name = 'books/book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, pk=kwargs['pk'])
        context.update({
            'book': book,
        })

        return context

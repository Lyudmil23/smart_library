from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView

from smart_library.books.forms import RentBookForm
from smart_library.books.models import Book, RentBook


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


@login_required
def rent_book(request, pk, *args, **kwargs):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return render(request, "404.html")

    form = RentBookForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Checking if the user has already rented this book
            if RentBook.objects.filter(user=request.user, book=book).exists():
                messages.error(request, "You have already rented this book.")
            else:
                rent_book = form.save(commit=False)
                rent_book.user = request.user
                rent_book.book = book
                rent_book.save()
                return redirect('home')

    context = {
        'book': book,
        'form': form,
    }
    return render(request, "books/rent_book.html", context)

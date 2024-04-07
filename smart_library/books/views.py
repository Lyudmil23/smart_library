from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.db.models.functions import Coalesce
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView

from smart_library.books.forms import RentBookForm
from smart_library.books.models import Book, RentBook
from smart_library.common.pagination_mixin import PaginationMixin
from smart_library.reviews.models import Review


class BooksView(PaginationMixin, ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'
    paginate_by = 6

    def get_queryset(self):
        books_average_rate = Book.objects.prefetch_related("reviews").annotate(avg_rate=Coalesce(Avg('reviews__rate'), 0.0)).all().order_by("created_at")
        return books_average_rate


class BookDetailsView(TemplateView):
    template_name = 'books/book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, pk=kwargs['pk'])
        reviews = Review.objects.filter(book_id=book.id).all()

        book_average_rate = Book.objects.filter(id=book.id).prefetch_related("reviews").annotate(avg_rate=Coalesce(Avg('reviews__rate'), 0.0)).first().avg_rate
        context.update({
            'book': book,
            'reviews': reviews,
            'avg_rate': book_average_rate,
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
                return redirect('rented books')

    context = {
        'book': book,
        'form': form,
    }
    return render(request, "books/rent_book.html", context)


class RentedBooksView(LoginRequiredMixin, ListView):
    model = RentBook
    template_name = 'books/rented_books.html'
    context_object_name = 'rented_books'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

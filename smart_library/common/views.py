from django.db.models import Avg
from django.db.models.functions import Coalesce
from django.shortcuts import render

from smart_library.books.models import Book


def home(request):
    books_average_rate = Book.objects.prefetch_related("reviews").annotate(
        avg_rate=Coalesce(Avg('reviews__rate'), 0.0)
    )

    # Ordering books by average rating in descending order
    top_books = books_average_rate.order_by("-avg_rate")[:3]

    context = {
        'top_books': top_books,
    }

    return render(request, 'common/home.html', context)

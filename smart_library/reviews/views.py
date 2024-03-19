from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from smart_library.books.models import Book
from smart_library.reviews.forms import ReviewBookForm
from smart_library.reviews.models import Review


@login_required
def review_book(request, pk, *args, **kwargs):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return render(request, "404.html")

    form = ReviewBookForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Checking if the user has already reviewed this book
            if Review.objects.filter(user=request.user, book=book).exists():
                messages.error(request, "Oops! It looks like you've already reviewed this book. Feel free to edit your existing review if needed.")
            else:
                review = form.save(commit=False)
                review.user = request.user
                review.book = book
                review.save()
                return redirect('book details', pk=book.pk)

    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'reviews/review_book.html', context)


class ReviewBooksView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

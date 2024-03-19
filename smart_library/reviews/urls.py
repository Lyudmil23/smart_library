from django.urls import path

from smart_library.reviews.views import review_book, ReviewBooksView

urlpatterns = [
    path('book/<int:pk>/review/', review_book, name='review book'),
    path('reviews/', ReviewBooksView.as_view(), name='reviews'),

]
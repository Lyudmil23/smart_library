from django.urls import path, include

from smart_library.reviews.views import review_book, ReviewBooksView, ReviewEditView, ReviewDeleteView

urlpatterns = [
    path('book/<int:pk>/review/', review_book, name='review book'),
    path('', ReviewBooksView.as_view(), name='reviews'),
    path('review/', include([
        path('edit/<int:pk>/', ReviewEditView.as_view(), name='edit review'),
        path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete review'),
    ])),

]
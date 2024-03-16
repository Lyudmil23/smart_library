from django.urls import path

from smart_library.authors.views import AuthorsListView

urlpatterns = [
    path('', AuthorsListView.as_view(), name='authors')

]
from django.shortcuts import render
from django.views.generic import ListView

from smart_library.authors.models import Author


class AuthorsListView(ListView):
    model = Author
    template_name = 'authors/authors_list.html'
    context_object_name = 'authors_list'
    paginate_by = 12



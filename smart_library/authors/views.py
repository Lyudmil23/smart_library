from django.shortcuts import render
from django.views.generic import ListView

from smart_library.authors.models import Author
from smart_library.common.pagination_mixin import PaginationMixin
from smart_library.common.queryset_mixin import OrderedQuerysetMixin


class AuthorsListView(OrderedQuerysetMixin, PaginationMixin, ListView):
    model = Author
    template_name = 'authors/authors.html'
    context_object_name = 'authors'
    paginate_by = 9



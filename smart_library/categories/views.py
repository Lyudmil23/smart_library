from django.shortcuts import render
from django.views.generic import ListView

from smart_library.categories.models import Category
from smart_library.common.pagination_mixin import PaginationMixin


class CategoriesView(PaginationMixin, ListView):
    model = Category
    template_name = 'categories/categories.html'
    context_object_name = 'categories'
    paginate_by = 6


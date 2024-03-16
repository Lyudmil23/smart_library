from django.shortcuts import render
from django.views.generic import ListView

from smart_library.categories.models import Category


class CategoriesView(ListView):
    model = Category
    template_name = 'categories/categories.html'
    context_object_name = 'categories_list'

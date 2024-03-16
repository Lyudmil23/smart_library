from django.urls import path

from smart_library.categories.views import CategoriesView

urlpatterns = [
    path('', CategoriesView.as_view(), name='categories')

]
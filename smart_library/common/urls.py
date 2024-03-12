from django.urls import path

from smart_library.common.views import home

urlpatterns = [
    path('', home, name='home'),

]
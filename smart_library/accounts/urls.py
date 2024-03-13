from django.urls import path

from smart_library.accounts.views import AppUserRegistrationView

urlpatterns = [
    path('register/', AppUserRegistrationView.as_view(), name='register user'),

]
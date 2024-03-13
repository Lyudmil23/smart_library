from django.urls import path

from smart_library.accounts.views import AppUserRegistrationView, AppUserLoginView

urlpatterns = [
    path('register/', AppUserRegistrationView.as_view(), name='register user'),
    path('login/', AppUserLoginView.as_view(), name='login user'),

]
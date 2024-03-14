from django.urls import path

from smart_library.accounts.views import AppUserRegistrationView, AppUserLoginView, AppUserLogoutView

urlpatterns = [
    path('register/', AppUserRegistrationView.as_view(), name='register user'),
    path('login/', AppUserLoginView.as_view(), name='login user'),
    path('logout/', AppUserLogoutView.as_view(), name='logout user'),

]
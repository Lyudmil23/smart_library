from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from smart_library.accounts.forms import AppUserRegistrationForm, AppUserLoginForm
from smart_library.accounts.models import AppUser


class AppUserRegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = AppUserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AppUserLoginForm


class AppUserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class AppUserDetailsView(LoginRequiredMixin, DetailView):
    model = AppUser
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'


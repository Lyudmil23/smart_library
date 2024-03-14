from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from smart_library.accounts.forms import AppUserRegistrationForm, AppUserLoginForm, ProfileEditForm
from smart_library.accounts.models import AppUser, Profile


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
    context_object_name = 'user'


class AppUserEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit.html'
    form_class = ProfileEditForm
    context_object_name = 'profile'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })


class AppUserDeleteView(LoginRequiredMixin, DeleteView):
    model = AppUser
    template_name = 'accounts/profile-delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('home')
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from smart_library.accounts.access_mixin import CustomAccessMixin
from smart_library.accounts.forms import AppUserRegistrationForm, AppUserLoginForm, ProfileEditForm, ChangePasswordForm
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


class AppUserDetailsView(LoginRequiredMixin, CustomAccessMixin, DetailView):
    model = AppUser
    template_name = 'accounts/profile-details.html'
    context_object_name = 'user'


class AppUserEditView(LoginRequiredMixin, CustomAccessMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit.html'
    form_class = ProfileEditForm
    context_object_name = 'profile'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })

    def form_valid(self, form):
        new_username = form.cleaned_data.get('username')
        user = self.request.user

        # Checking if the new username exceeds the maximum length
        max_length = AppUser._meta.get_field('username').max_length
        if len(new_username) > max_length:
            messages.error(self.request, f'Username cannot exceed {max_length} characters.')
            return self.form_invalid(form)

        # Checking if the new username is unique
        if AppUser.objects.exclude(pk=user.pk).filter(username=new_username).exists():
            # If is not unique, we are displaying error message
            messages.error(self.request, 'This username is already taken. Please choose a different one.')
            return self.render_to_response(self.get_context_data(form=form))

        # Checking if the new email is unique
        new_email = form.cleaned_data.get('email')
        if AppUser.objects.exclude(pk=user.pk).filter(email=new_email).exists():
            # If is not unique, we are displaying error message
            messages.error(self.request, 'This email is already taken. Please choose a different one.')
            return self.render_to_response(self.get_context_data(form=form))

        return super().form_valid(form)


class AppUserDeleteView(LoginRequiredMixin, CustomAccessMixin, DeleteView):
    model = AppUser
    template_name = 'accounts/profile-delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('home')


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change-password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')



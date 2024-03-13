from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from smart_library.accounts.forms import AppUserRegistrationForm


class AppUserRegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = AppUserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result

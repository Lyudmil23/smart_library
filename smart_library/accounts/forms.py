from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator

from smart_library.accounts.models import AppUser, Profile


class AppUserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        validators=[MinLengthValidator(2), RegexValidator(r'^[a-zA-Z]*$', 'The name should contain only letters!')])
    last_name = forms.CharField(
        validators=[MinLengthValidator(2), RegexValidator(r'^[a-zA-Z]*$', 'The name should contain only letters!')])

    class Meta:
        model = AppUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def save(self, commit=True):
        user = super().save(commit=commit)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            user=user,
        )

        if commit:
            profile.save()

        return user


class AppUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'first_name', 'last_name', 'gender', 'profile_image')

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username
        self.fields['email'].initial = self.instance.user.email

    def save(self, *args, **kwargs):
        profile = super(ProfileEditForm, self).save(*args, **kwargs)
        profile.user.username = self.cleaned_data['username']
        profile.user.email = self.cleaned_data['email']
        profile.user.save()
        return profile


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = AppUser
        fields = ('old_password', 'new_password1', 'new_password2')

    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your old password'}
        )
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your new password'}
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm your new password'}
        )
    )







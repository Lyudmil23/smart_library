from django.urls import path, include

from smart_library.accounts.views import AppUserRegistrationView, AppUserLoginView, AppUserLogoutView, \
    AppUserDetailsView, AppUserEditView, AppUserDeleteView

urlpatterns = [
    path('register/', AppUserRegistrationView.as_view(), name='register'),
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('logout/', AppUserLogoutView.as_view(), name='logout'),

    path('profile/<int:pk>/', include([
        path('', AppUserDetailsView.as_view(), name='profile details'),
        path('edit/', AppUserEditView.as_view(), name='profile edit'),
        path('delete/', AppUserDeleteView.as_view(), name='profile delete'),
    ])),

]
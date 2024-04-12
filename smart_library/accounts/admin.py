from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import PermissionDenied
from django.utils.html import format_html

# from smart_library.accounts.forms import ProfileForm
from smart_library.accounts.models import AppUser, Profile


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('username', 'email')
    list_filter = ('date_joined', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('date_joined', )
    list_per_page = 10

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    readonly_fields = ('date_joined',)  # Marking date_joined as non-editable


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        if object.profile_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50px;"/>'.format(object.profile_image.url))
        else:
            return '-'

    thumbnail.short_description = 'Profile Thumbnail'

    list_display = ('first_name', 'last_name', 'thumbnail', 'gender', 'profile_image', 'user')
    list_display_links = ('first_name', 'user')
    list_filter = ('first_name', 'last_name', 'gender')
    search_fields = ('first_name', 'last_name', 'gender')
    ordering = ('user', )
    list_per_page = 10

    # Disabling the ability to add profiles
    def has_add_permission(self, request):
        return False

    #Disabling the ability to delete profiles
    def has_delete_permission(self, request, obj=None):
        # Checking if deletion is performed from the User model
        if request.path.startswith('/admin/accounts/appuser/'):
            return True
        return False

    #Disabling the user field in profile
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(ProfileAdmin, self).get_readonly_fields(request, obj))
        readonly_fields.append('user')
        return readonly_fields
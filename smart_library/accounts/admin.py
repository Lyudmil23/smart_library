from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from smart_library.accounts.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('username', 'email')
    list_filter = ('username', 'date_joined', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('date_joined', )

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
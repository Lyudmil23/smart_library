from django.contrib import admin

from smart_library.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('name', )
    search_fields = ('name', )
    ordering = ('name', )

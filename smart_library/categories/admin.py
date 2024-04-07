from django.contrib import admin

from smart_library.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'books_in_category')
    list_filter = ('name', )
    search_fields = ('name', )
    ordering = ('id', )
    list_per_page = 10

    def books_in_category(self, obj):
        return ", ".join([book.book_title for book in obj.book_set.all()])

    books_in_category.short_description = 'Books'

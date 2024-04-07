from django.contrib import admin

from smart_library.authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'books_by_author')
    list_display_links = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
    ordering = ('id',)
    search_fields = ('first_name', 'last_name')
    list_per_page = 15

    def books_by_author(self, obj):
        return ", ".join([book.book_title for book in obj.books.all()])

    books_by_author.short_description = 'Books'
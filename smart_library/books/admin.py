from django.contrib import admin
from django.utils.html import format_html

from smart_library.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src="{}" width="50" height="50" style="border-radius: 50px;"/>'.format(object.book_image.url))

    thumbnail.short_description = 'Book Image'

    list_display = ('id', 'book_title', 'thumbnail', 'category', 'author')
    list_display_links = ('id', 'book_title', 'thumbnail',)
    list_filter = ('book_title', 'category', 'author')
    ordering = ('id', )
    search_fields = ('book_title', 'category__name', 'author__first_name', 'author__last_name')


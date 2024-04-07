from django.contrib import admin
from django.utils.html import format_html

from smart_library.books.models import Book, RentBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src="{}" width="50" height="50" style="border-radius: 50px;"/>'.format(object.book_image.url))

    thumbnail.short_description = 'Book Image'

    list_display = ('id', 'book_title', 'thumbnail', 'category', 'author')
    list_display_links = ('id', 'book_title', 'thumbnail',)
    list_filter = ('category', 'author')
    ordering = ('id', )
    search_fields = ('book_title', 'category__name', 'author__first_name', 'author__last_name')
    list_per_page = 10


@admin.register(RentBook)
class RentBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'created_at', 'period_start', 'period_end')
    list_display_links = ('user', 'book')
    list_filter = ('user', 'book', 'created_at', 'period_start', 'period_end')
    ordering = ('id', )
    search_fields = ('user__username', 'book__book_title')
    list_per_page = 10



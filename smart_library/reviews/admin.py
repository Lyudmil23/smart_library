from django.contrib import admin

from smart_library.reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rate', 'comment')
    list_display_links = ('user', 'book')
    list_filter = ('user', 'book')
    ordering = ('id', )
    search_fields = ('user__username', 'book__book_title')
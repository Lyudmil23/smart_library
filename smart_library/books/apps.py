from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smart_library.books'

    def ready(self):
        import smart_library.books.signals


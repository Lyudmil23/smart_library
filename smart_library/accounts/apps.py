from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smart_library.accounts'

    # Importing the signals
    def ready(self):
        import smart_library.accounts.signals

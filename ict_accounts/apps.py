from django.apps import AppConfig


class IctAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ict_accounts'
    
    def ready(self):
        import ict_accounts.signals


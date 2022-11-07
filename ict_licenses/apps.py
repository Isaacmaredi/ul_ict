from django.apps import AppConfig


class IctLicensesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ict_licenses'
    
    def ready(self):
        import ict_licenses.signals

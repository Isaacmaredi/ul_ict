from django.apps import AppConfig


class IctProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ict_projects'

    # def ready(self):
    #     import ict_projects.signals
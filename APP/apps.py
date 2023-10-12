from django.apps import AppConfig


class APPConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'APP'

    def ready(self):
        import APP.signals  # Reemplaza 'tu_app' por el nombre de tu aplicación

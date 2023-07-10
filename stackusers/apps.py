from django.apps import AppConfig


class StackusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stackusers'

#Import signals.py
    def ready(self): 
        import stackusers.signals

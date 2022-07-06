from django.apps import AppConfig

class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.crm'

    def ready(self):
        from jobs.scheduler import ClientJobScheduler

        ClientJobScheduler.start()

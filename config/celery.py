import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'email': {
        'task': 'src.core.tasks.send_email_task',
        'schedule': 600.0
    },
}
app.conf.timezone = 'UTC'

from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
# from ict_tasks.tasks import license_renewal_notify
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ict_main.settings')

app = Celery('ict_main')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()  


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
app.conf.beat_schedule = {
    'send-email-every-single-minute': {
        'task': 'ict_tasks.tasks.license_renewal_notify',
        'schedule': crontab(hour = 23, minute = 18),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight 
    },
}
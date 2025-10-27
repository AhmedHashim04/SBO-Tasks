import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



from celery.schedules import crontab  
app.conf.beat_schedule = {
    'run-notify-every-30-seconds': {
        'task': 'app.tasks.notify_sending',
        'schedule': 30.0,  # كل 30 ثانية
        'args': (5, 7),    # باراميترات للمهمة
    },
    'run-every-midnight': {
        'task': 'app.tasks.notify_sending',
        'schedule': crontab(hour=0, minute=0),  # كل يوم الساعة 00:00
        'args': (10, 20),
    },
}

# celery -A project beat -l info
# if u change the schedule and want to apply it without stopping the beat service, run:
# rm celerybeat-schedule
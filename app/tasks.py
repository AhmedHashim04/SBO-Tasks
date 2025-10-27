# Create your tasks here

from celery import shared_task


@shared_task
def notify_sending(x, y):
    print('celery task notify_sending called with', x, y)
    return x + y

# celery -A project worker -l info 
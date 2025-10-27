# Create your tasks here

from celery import shared_task


@shared_task
def add(x, y):
    print('celery task add called with', x, y)
    return x + y

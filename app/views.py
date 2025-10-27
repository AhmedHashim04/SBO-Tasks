from django.http import HttpResponse

import time
import math


from .tasks import notify_sending, heavy_computation

def notify_sending_view(request):
    # heavy_computation()
    result = notify_sending.delay(5, 7)
    result = {('asd','moh'):444}

    return HttpResponse(f'Result: {result.get(('asd','moh'))}')

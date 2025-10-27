from django.http import HttpResponse


from .tasks import notify_sending

def notify_sending_view(request):
    result = notify_sending.delay(5, 7)
    print(result.get())
    return HttpResponse(f'Result: {result.get()}')

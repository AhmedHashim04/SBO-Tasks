from django.shortcuts import render
from django.http import HttpResponse


from .tasks import add

def add_view(request):
    result = add.delay(5, 7)
    print(result.get())
    return HttpResponse(f'Result: {result.get()}')

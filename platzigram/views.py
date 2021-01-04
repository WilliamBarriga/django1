from django.http import HttpResponse
from datetime import datetime
import json


def date_time(request):
    now = datetime.now().strftime('%b %d, %Y - %H:%M horas')
    return HttpResponse(f'la fecha es {now}')


def numbers(request):
    numbers = sorted(int(number) for number in request.GET['numbers'].split(','))
    data = {
        'numbers' : numbers 
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = f'<h2>lo siento {name} no puedes ingresar</h2>'
    else:
        message = f'hola {name} bienvenido'
    
    return HttpResponse(message)
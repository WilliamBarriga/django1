from django.http import HttpResponse
from django.urls import path

def hello_world(request):
    return HttpResponse('Hello_world!')

urlpatterns = [
    path('hello-world/', hello_world)
]

from platzigram import views
from django.urls import path

urlpatterns = [
    path('hello-world/', views.date_time),
    path('numbers/', views.numbers),
    path('validation/<str:name>/<int:age>/', views.say_hi)
]

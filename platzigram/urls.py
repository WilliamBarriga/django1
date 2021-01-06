from platzigram import views as local_views
from django.urls import path
from posts import views as posts_views

urlpatterns = [
    path('hello-world/', local_views.date_time),
    path('numbers/', local_views.numbers),
    path('validation/<str:name>/<int:age>/', local_views.say_hi),
    path('posts/', posts_views.list_posts)
]

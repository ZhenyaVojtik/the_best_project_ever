from django.urls import path
from manager.views import hello, man, findbook

# hello/
urlpatterns = [
    path("hello/", hello),
    path("man/", man),
    path('findbook/', findbook)
]


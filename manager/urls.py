from django.urls import path
from manager.views import hello, MyPage

# hello/
urlpatterns = [
    path("hello/<int:digit>/", hello),
    path("man/<str:name>/", hello),
    path('findbook/', hello),
    path('', MyPage.as_view(), name='the-main-page'),
]


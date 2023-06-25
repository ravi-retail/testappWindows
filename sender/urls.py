
from django.urls import path, include
from .views import sum

urlpatterns = [
    path('sum', sum),
]

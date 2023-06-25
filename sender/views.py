from django.shortcuts import render, HttpResponse
from .tasks import add

# Create your views here.
def sum(request):
    add.delay(2, 7)
    return HttpResponse("Called the sum")

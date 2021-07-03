from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, World! <br> This is task03.2 18 stream homework solution.")

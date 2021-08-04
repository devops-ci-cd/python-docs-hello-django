from django.http import HttpResponse
from django.shortcuts import render
import os

def hello(request):
    return HttpResponse("Hello, World! <br> CloudX solution <br> from center-us location <br>" + str(os.environ))

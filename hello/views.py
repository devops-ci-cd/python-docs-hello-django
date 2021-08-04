from django.http import HttpResponse
from django.shortcuts import render
import os

def hello(request):
    return HttpResponse("Hello, World! <br> CloudX solution <br> from east-us location <br> Connections string: <br>" + str(os.environ['ConVar']))

from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
    # for index.html health probe purpose
    path('index.html/', views.hello, name='hello'),
]

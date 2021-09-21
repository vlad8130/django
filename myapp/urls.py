from django.urls import path

from .views import index, first



urlpatterns = [
    path('', index, name='index'),
path('first', first, name='first'),
]

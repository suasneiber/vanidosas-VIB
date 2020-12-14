from django.urls import path
from apps.curso.views import index

urlpatterns = [
    path(r'^$', index),
]

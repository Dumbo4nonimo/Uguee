# api/urls.py
from django.urls import path
from .views import welcome

urlpatterns = [
    path('', welcome, name='api_welcome'),
]

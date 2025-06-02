# api/urls.py
from django.urls import path
from .views import welcome, protected_view

urlpatterns = [
    path('', welcome, name='api_welcome'),
    path('protegido/', protected_view, name='protected_view'),
]

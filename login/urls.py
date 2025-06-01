from django.urls import path
from . import views
from login.views import CustomLoginView

urlpatterns = [
    path('register/<str:role>/', views.role_register_view, name='role_register'),
    path('', CustomLoginView.as_view(), name='custom-login'),
]

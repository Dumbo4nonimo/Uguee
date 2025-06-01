from django.urls import path, include
from typeUser.views import register_view, index
from login.views import CustomLoginView

urlpatterns = [
    path('', index, name='typeuser-index'),
    path('typeUser/', register_view, name='register'),  
    path('login/', CustomLoginView.as_view(), name='login'),  
]
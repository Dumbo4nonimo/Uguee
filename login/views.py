from django.shortcuts import render
from django.http import Http404

def role_register_view(request, role):
    if role not in ['student', 'driver', 'institution']:
        raise Http404("Rol no válido")

    return render(request, f'login/register_{role}.html', {'role': role})

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login/login.html'  # Usa tu plantilla personalizada

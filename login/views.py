from django.shortcuts import render, redirect
from django.http import Http404
from .forms import UserForm, StudentForm, DriverForm, InstitutionForm
from django.contrib.auth.views import LoginView
from api.models import Institution

def role_register_view(request, role):
    if role not in ['student', 'driver', 'institution']:
        raise Http404("Rol no válido")

    user_form = UserForm()
    if role == 'institution':
        user_form.fields.pop('username')  # Elimina el campo username solo para institución

    role_form = {
        'student': StudentForm(),
        'driver': DriverForm(),
        'institution': InstitutionForm(),
    }[role]

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if role == 'institution':
            user_form.fields.pop('username')  # Elimina el campo username solo para institución


        role_form = {
            'student': StudentForm(request.POST),
            'driver': DriverForm(request.POST),
            'institution': InstitutionForm(request.POST),
        }[role]

        if user_form.is_valid() and role_form.is_valid():
            # Guarda el usuario
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.role = role
            user.save()
            # Guarda el perfil según el rol
            profile = role_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('/api/')  # Redirige a mensaje de bienvenida

    return render(request, f'login/register_{role}.html', {
        'user_form': user_form,
        'role_form': role_form,
        'role': role,
    })

class CustomLoginView(LoginView):
    template_name = 'login/login.html'

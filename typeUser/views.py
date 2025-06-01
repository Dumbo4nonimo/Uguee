from django.shortcuts import render, redirect

def register_view(request):
    roles = [
        ('student', 'Estudiante'),
        ('driver', 'Conductor'),
        ('institution', 'Institución'),
        # se muestra 'admin'
    ]
    return render(request, 'typeUser/register.html', {'roles': roles})


def index(request):
    return render(request, 'typeUser/index.html')



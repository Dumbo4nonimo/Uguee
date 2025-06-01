from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from api.models import User, Student, Driver, Institution

User = get_user_model()

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'phone', 'address']

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['code', 'faculty', 'degree']

class DriverRegisterForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['cc', 'institution_card', 'license', 'state', 'institution_fk']

class InstitutionRegisterForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['official_name', 'logo', 'colors_set', 'state']

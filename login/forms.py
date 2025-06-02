from django import forms
from api.models import Student, Driver, Institution
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': None,
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['code', 'faculty', 'degree']

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['official_name', 'adreess', 'logo', 'colors_set', 'state']

class DriverForm(forms.ModelForm):
    institution_fk = forms.ModelChoiceField(
        queryset=Institution.objects.all(),
        label='Institución',
        empty_label="Seleccione una institución"
    )

    class Meta:
        model = Driver
        fields = ['cc', 'institution_card', 'license', 'state', 'institution_fk']

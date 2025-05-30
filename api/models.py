from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_7_characters, is_numeric, length_limit

# Models
class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Estudiante'),
        ('conductor', 'Conductor'),
        ('institution', 'Institucion'),
        ('admin', 'Administrador'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, validators=[is_numeric])
    address = models.CharField(max_length=255, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(
        max_length=7,
        unique=True,
        validators=[validate_7_characters, is_numeric],
    )
    faculty = models.CharField(max_length=100, validators=[is_numeric])
    degree = models.CharField(max_length=100, validators=[is_numeric])

class Institution(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    official_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    logo = models.TextField(validators=[length_limit])
    colors_set = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    institution_fk = models.ForeignKey(Institution, on_delete=models.CASCADE)
    cc = models.CharField(max_length=10 ,unique=True, validators=[is_numeric])
    institution_card = models.CharField(max_length=100)
    license = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

class Passenger(models.Model):
    user_fk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_code = models.ForeignKey(Student, to_field='code', on_delete=models.CASCADE)

#class Passenger(models.Model):
#    conductor_fk = models.ForeignKey(Conductor, on_delete=models.CASCADE)
#    student_code = models.ForeignKey(Student, to_field='code', on_delete=models.CASCADE)
#Opcion2

class Admin(models.Model):
    user_fk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    institution_fk = models.ForeignKey(Institution, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=50)

class Vehicle(models.Model):
    conductor_fk = models.ForeignKey(Driver, on_delete=models.CASCADE)
    QR_vehicle = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    plate = models.CharField(max_length=20)
    soat = models.DateField()
    tecno = models.DateField()

class Route(models.Model):
    origin = models.CharField(max_length=255)
    destiny = models.CharField(max_length=255)
    description = models.TextField(validators=[length_limit])

class Location(models.Model):
    vehicle_fk = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route_fk = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateTimeField()
    coordinates = models.CharField(max_length=100)

class Travel(models.Model):
    vehicle_fk = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route_fk = models.ForeignKey(Route, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    startPoint = models.CharField(max_length=255)
    date_to_out = models.DateTimeField(auto_now_add=True)

class PassengerTravel(models.Model):
    user_fk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    travel_fk = models.ForeignKey(Travel, on_delete=models.CASCADE)

class PassengerRoute(models.Model):
    user_fk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    route_fk = models.ForeignKey(Route, on_delete=models.CASCADE)

class Validation(models.Model):
    travel_fk = models.ForeignKey(Travel, on_delete=models.CASCADE)
    user_fk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    validation_state = models.CharField(max_length=50)
    validation_date = models.DateTimeField(auto_now_add=True)

class Grade(models.Model):
    travel_fk = models.ForeignKey(Travel, on_delete=models.CASCADE)
    passenger_fk = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    score = models.SmallIntegerField()
    comment = models.TextField(validators=[length_limit])
    grade_date = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    admin_fk = models.ForeignKey(Admin, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    date = models.DateTimeField()

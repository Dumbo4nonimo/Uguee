import re
from django.forms import ValidationError

def validate_7_characters(value):
    if len(value) != 7:
        raise ValidationError("El código debe tener exactamente 7 caracteres.")

def is_numeric(value): 
    if not re.match(r'^[0-9\s]+$', value): 
        raise ValidationError('Este campo solo permite números.')
    
def length_limit(value):
    if len(value) > 500:
        raise ValidationError('No exceder más de 500 caracteres')

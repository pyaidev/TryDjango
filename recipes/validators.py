from django.core.exceptions import ValidationError

validate_units = ['kg', 'l', 'sht']

def validator_of_units(value):
    if value not in validate_units:
        raise ValidationError(f'{value} is not a valid unit')


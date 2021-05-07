from django.core import validators
from django.core.exceptions import ValidationError
import re

def char_validation1(values1):
    if len(values1)>4:
        if all(x.isalpha() for x in values1):
            pass

    else:
        raise ValidationError('Only Charcter Minmum 4 letters')

def char_validation2(values2):
    if len(values2)>4:
        if all(x.isalpha() for x in values2):
            pass
    else:
        raise ValidationError('Only Charcter Minmum 4 letters')
 
import re
from django.core.exceptions import ValidationError


def validate_isbn(value):
    isbn10_pattern = r"^\d{9}[\dX]$"
    isbn13_pattern = r"^\d{13}$"
    if not (re.match(isbn10_pattern, value) or re.match(isbn13_pattern, value)):
        raise ValidationError("Invalid ISBN number. It must be ISBN-10 or ISBN-13.")

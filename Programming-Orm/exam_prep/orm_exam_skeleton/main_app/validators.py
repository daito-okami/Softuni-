from django.core.exceptions import ValidationError


def validate_len_2(value):
    if len(value) < 2 :
        raise ValidationError("")


def validate_max_120(value):
    if value > 120:
        raise ValidationError("")

def validate_max_150value(value):
    if value > 150:
        raise ValidationError("")

def validate_max_50value(value):
    if value > 50:
        raise ValidationError("")


def validate_len_5(value):
    if len(value) < 5 :
        raise ValidationError("")

def rating_validator(value):
    if 0 > value > 10.0:
        raise ValidationError("")
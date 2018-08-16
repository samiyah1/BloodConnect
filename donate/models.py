from django.db import models
from django.core.validators import RegexValidator

class BloodBank(models.Model):
    name = models.CharField(max_length = 130)
    location = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+254123456789'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list 
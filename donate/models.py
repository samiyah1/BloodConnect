from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=40)
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE')
    )
    gender = models.CharField(max_length=10,null=True,choices=GENDER)
    A_POSITIVE = 'A_POSITIVE'
    A_NEGATIVE = 'A_NEGATIVE'
    B_POSITIVE = 'B_POSITIVE'
    B_NEGATIVE = 'B_NEGATIVE'
    O_POSITIVE = 'O_POSITIVE'
    O_NEGATIVE = 'O_NEGATIVE'
    AB_POSITIVE = 'AB_POSITIVE'
    AB_NEGATIVE = 'AB_NEGATIVE'
    BLOOD_GROUPS = (
        (A_POSITIVE,'A +'),
        (A_NEGATIVE,'A -'),
        (B_POSITIVE,'B +'),
        (B_NEGATIVE,'B -'),
        (O_POSITIVE,'O +'),
        (O_NEGATIVE,'O -'),
        (AB_POSITIVE,'AB +'),
        (AB_NEGATIVE,'AB -')
    )
    blood_type = models.CharField(max_length=20,null=True,choices=BLOOD_GROUPS)
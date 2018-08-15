from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
   if created:
       Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   instance.profile.save()
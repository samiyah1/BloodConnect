from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import BloodBank
from django.contrib.auth import get_user_model

User = get_user_model()
class DonorSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone_number', 'gender', 'blood_type')

class BankSignupForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ('name', 'location', 'email', 'phone_number')

from django import forms
from . models import BloodBank

class BankSignupForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ('name', 'location', 'email', 'phone_number')
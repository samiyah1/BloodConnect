from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm
from . models import Donation
from django.contrib.auth import get_user_model

User = get_user_model()
class DonorSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone_number', 'gender', 'blood_type')

class BankSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','location','phone_number')


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['message', 'location', 'starts_at', 'ends_at']

    starts_at = forms.DateField(widget = forms.DateInput(attrs = {'type':'date'}))
    ends_at = forms.DateField(widget = forms.DateInput(attrs = {'type':'date'}))

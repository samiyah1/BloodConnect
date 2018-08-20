from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm
from . models import BloodBank, Donation
from django.contrib.auth import get_user_model

User = get_user_model()
class DonorSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone_number', 'gender', 'blood_type')

class BankSignupForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label = "Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Password confirmation", widget = forms.PasswordInput,
    help_text = "Enter the same password as above, for verification.")


    class Meta:
        model = BloodBank
        fields = ('username', 'location', 'email', 'phone_number')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code = 'password_mismatch'
            )
        return password2

    def save(self, commit = True):
        user = super(BankSignupForm, self).save(commit = False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['message', 'location', 'starts_at', 'ends_at']

    starts_at = forms.DateField(widget = forms.DateInput(attrs = {'type':'date'}))
    ends_at = forms.DateField(widget = forms.DateInput(attrs = {'type':'date'}))

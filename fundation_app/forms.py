from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from fundation_app.models import Donation


class DonationModelForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'


class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-group'}), label='Imię')
    last_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-group'}), label='Nazwisko')
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-group'}), label='Email')
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-group'}), label='Hasło')
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-group'}), label='Powtórz Hasło')

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError('Passwords are not the same.')

        return data

from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from fundation_app.models import Donation


class DonationModelForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-group',
                                                                               'placeholder': 'Imię'}), label='')
    last_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-group',
                                                                              'placeholder': 'Nazwisko'}), label='')
    email = forms.EmailField(max_length=128, widget=forms.EmailInput(attrs={'class': 'form-group',
                                                                            'placeholder': 'Email'}), label='')
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-group',
                                                                                  'placeholder': 'Hasło'}), label='')
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-group',
                                                                                  'placeholder': 'Powtórz hasło'}),
                                label='')

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError('Hasła nie są takie same')

        return data


class LoginForm(forms.ModelForm):
    username = forms.EmailField(max_length=128, widget=forms.EmailInput(attrs={'class': 'form-group',
                                                                               'placeholder': 'Email'}), label='')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-group',
                                                                                 'placeholder': 'Hasło'}), label='')

    class Meta:
        model = User
        fields = ['username', 'password']

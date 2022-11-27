from django.contrib.auth.models import User
from django import forms

from fundation_app.models import Donation


class DonationModelForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'

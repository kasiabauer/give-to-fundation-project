from django.shortcuts import render, redirect
from django.views import View

from fundation_app.forms import DonationModelForm
from fundation_app.models import Donation, Category


def get_bag_quantity():
    bag_quantity = Donation.objects.all()
    # all_donations_with_bags = Donation.objects.get(quantity__gte=0)
    # bag_quantity = 0
    # for donation in all_donations_with_bags:
    #     bag_quantity += donation.quantity
    return bag_quantity


class LandingPageView(View):

    def get(self, request):
        donated_bags = get_bag_quantity()
        supported_organizations = 0
        return render(request, 'index.html', {
            'donated_bags': donated_bags, 'supported_organizations': supported_organizations})


class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')


class AddDonationView(View):

    def get(self, request):
        return render(request, 'form.html')


class FormConfirmView(View):

    def get(self, request):
        return render(request, 'form-confirmation.html')


class CreateInstitutionView(View):

    def get(self, request):
        form = DonationModelForm()
        return render(request, 'form-item.html', {'form': form})

    def post(self, request):
        form = DonationModelForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.save()
            return redirect('landing-page')
        else:
            return render(request, 'form-item.html', {'form': form})

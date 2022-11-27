from django.shortcuts import render, redirect
from django.views import View

from fundation_app.forms import DonationModelForm
from fundation_app.models import Donation, Category, Institution, INSTITUTION_TYPE


def get_bags():
    all_donations_with_bags = Donation.objects.filter(quantity__gte=0)
    bag_quantity = 0
    for donation in all_donations_with_bags:
        bag_quantity += donation.quantity
    return bag_quantity


def get_supported_organizations():
    organizations = Donation.objects.order_by().values('institution').distinct()
    return organizations


def get_institutions():
    # institutions = Institution.objects.order_by().values('name', 'description', 'type', 'categories__name', )
    # .distinct()
    institutions = Institution.objects.filter().values('name', 'description', 'type', 'categories__name', )
    institutions_1 = Institution.objects.filter(type__contains=1).values('name', 'description', 'type',
                                                                         'categories__name', )
    institutions_2 = Institution.objects.filter(type__contains=2).values('name', 'description', 'type',
                                                                         'categories__name', )
    institutions_3 = Institution.objects.filter(type__contains=3).values('name', 'description', 'type',
                                                                         'categories__name', )
    return institutions, institutions_1, institutions_2, institutions_3


class LandingPageView(View):

    def get(self, request):
        donated_bags = get_bags()
        supported_organizations_number = len(get_supported_organizations())
        institutions = get_institutions()
        return render(request, 'index.html', {
            'donated_bags': donated_bags, 'supported_organizations': supported_organizations_number,
            'institutions1': institutions[1], 'institutions2': institutions[2], 'institutions3': institutions[3]})


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

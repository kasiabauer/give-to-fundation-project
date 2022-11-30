from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from fundation_app.forms import DonationModelForm, RegisterForm, LoginForm
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
    # institutions = Institution.objects.all.values('name', 'description', 'type', 'categories__name', )
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
            'institutions1': institutions[1], 'institutions2': institutions[2], 'institutions3': institutions[3],
            'institutions': institutions[0]})


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            u = User()
            u.username = email
            u.email = email
            u.first_name = first_name
            u.last_name = last_name
            u.set_password(password)
            u.save()
            return redirect('/login')
        return render(request, 'form.html', {'form': form})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                url = request.GET.get('next', '/')
                login(request, user)
                return redirect(url)
        else:
            return render(request, 'login.html', {'form': form, 'msg': 'nie udalo się zalogować'})


class LogoutView(View):

    def get(self, request):
        # user = request.user.username
        logout(request)
        return render(request, 'index.html')


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

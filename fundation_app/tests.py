import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from fundation_app.models import Donation


# 1st test checking the system
@pytest.mark.django_db
def test_001_check_settings():
    assert True


# 1st test for LandingPageview
@pytest.mark.django_db
def test_002_get_landing_page(client):
    url = reverse('landing-page')
    response = client.get(url)
    assert response.status_code == 200


# 1st test for Loginview
def test_003_get_login(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


# 1st test for Registerview
def test_004_get_register(client):
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200


# 1st test for AddDonationView
def test_005_get_add_donation(client):
    url = reverse('add-donation')
    response = client.get(url)
    assert response.status_code == 200


# 1st test for FormConfirmView
def test_006_get_form_confirm(client):
    url = reverse('form-confirm')
    response = client.get(url)
    assert response.status_code == 200


# 2nd test for LandingPageView
@pytest.mark.django_db
def test_007_category_model(client, categories):
    url = reverse('landing-page')
    category = categories[0]
    response = client.get(url)
    assert response.status_code == 200


# 3rd test for LandingPageView
@pytest.mark.django_db
def test_008_institution_model(client, categories, institutions):
    url = reverse('landing-page')
    category = categories[0]
    institution = institutions[0]
    print(institution)
    response = client.get(url)
    assert response.status_code == 200


# test for User model
@pytest.mark.django_db
def test_009_user_model(client, users):
    url = reverse('landing-page')
    user = users[0]
    response = client.get(url)
    assert response.status_code == 200


# test for Donation model
@pytest.mark.django_db
def test_010_donation_model(client, donations):
    url = reverse('landing-page')
    donation = donations[0]
    response = client.get(url)
    assert response.status_code == 200


# test for LandingPage View with donations data
@pytest.mark.django_db
def test_002_get_landing_page_with_donations(client, donations):
    url = reverse('landing-page')
    response = client.get(url)
    assert len(Donation.objects.all()) == 10
    assert response.status_code == 200

from datetime import datetime, time
from random import randint

import pytest
from django.contrib.auth.models import User

from fundation_app.models import Category, Institution, INSTITUTION_TYPE, Donation


@pytest.fixture
def categories():
    lst = []
    for category in range(10):
        category_name = 'Category_' + str(category)
        lst.append(Category.objects.create(name=category_name))

    return lst


@pytest.fixture
def institutions(categories):
    lst = []
    institution_type = 0
    for category in categories:
        institution_name = 'Institution for category ' + str(category)
        x = Institution.objects.create(
            name=institution_name,
            description='test description',
            type=INSTITUTION_TYPE[institution_type])
        x.categories.add(category)
        if institution_type < 2:
            institution_type += 1
        else:
            institution_type = 0
        lst.append(x)
    return lst


@pytest.fixture
def users():
    lst = []
    for user in range(10):
        user_name = 'User@' + str(user)
        lst.append(User.objects.create(username=user_name))
    return lst


@pytest.fixture
def user_with_pass():
    lst = []
    user_name = 'User@test.com'
    user_with_pass = User.objects.create(username=user_name, password='0testpass0')
    return user_with_pass


@pytest.fixture
def donations(users, categories):
    lst = []
    for user in users:
        phone = f'+48 500 500 0{randint(10, 99)}'
        institution = Institution.objects.create(
            name='institution_name',
            description='test description',
            type=INSTITUTION_TYPE[1])
        x = Donation.objects.create(
            quantity=1,
            address='test address 1',
            phone_number=phone,
            city='test city',
            zip_code='01-100',
            pick_up_date=datetime(22, 1, 1),
            pick_up_time=time(10, 0),
            pick_up_comment='test comment',
            institution=institution)
        x.categories.add(categories[0])
        print(x.phone_number, x.id)
        lst.append(x)
    return lst

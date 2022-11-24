import pytest

from fundation_app.models import Category, Institution, INSTITUTION_TYPE


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

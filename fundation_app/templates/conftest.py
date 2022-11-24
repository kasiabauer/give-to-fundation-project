import pytest

from fundation_app.models import Category


@pytest.fixture
def categories():
    lst = []
    for category in range(10):
        category_name = 'Category_' + str(category)
        lst.append(Category.objects.create(name=category_name))

    return lst

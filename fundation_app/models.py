from django.contrib.auth.models import User
from django.db import models

INSTITUTION_TYPE = (
    ('1', 'fundacja'),
    ('2', 'organizacja pozarządowa'),
    ('3', 'zbiórka lokalna')
)


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    type = models.CharField(choices=INSTITUTION_TYPE, default='fundacja', max_length=64)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name}'


class Donation(models.Model):
    quantity = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=64)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Donation id:{self.id}'

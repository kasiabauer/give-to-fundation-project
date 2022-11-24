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

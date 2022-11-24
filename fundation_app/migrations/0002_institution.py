# Generated by Django 4.1.3 on 2022-11-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundation_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('1', 'fundacja'), ('2', 'organizacja pozarządowa'), ('3', 'zbiórka lokalna')], default='fundacja', max_length=64)),
                ('categories', models.ManyToManyField(to='fundation_app.category')),
            ],
        ),
    ]
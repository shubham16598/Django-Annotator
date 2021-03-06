# Generated by Django 3.0.6 on 2020-05-29 06:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotatorbackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='annotation',
            field=models.TextField(validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Capital', regex='(^[A-Z][\\sa-z0-9]+$)|(^(\x08[A-Z]\\w*\\s*)+$)')]),
        ),
    ]

# Generated by Django 3.2 on 2022-11-20 12:12

import django.core.validators
from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, error_messages={'unique': 'شماره وارد شده قبلا ثبت شده است!'}, max_length=128, null=True, region=None, unique=True, validators=[django.core.validators.RegexValidator('^989[0-3,9]\\d{8}$', 'شماره همراه خود راد وارد کنید.', 'invalid')], verbose_name='تلفن همراه'),
        ),
    ]

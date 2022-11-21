# Generated by Django 3.2 on 2022-11-21 05:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, error_messages={'unique': 'شماره وارد شده قبلا ثبت شده است!'}, max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator('^1?\\d{9,15}$', 'شماره همراه خود راد وارد کنید.', 'invalid')], verbose_name='تلفن همراه'),
        ),
    ]

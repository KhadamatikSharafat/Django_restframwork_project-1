# Generated by Django 3.2 on 2022-11-22 08:38

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0014_alter_posregister_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posregister',
            name='first_shaba_number',
            field=models.CharField(max_length=26, validators=[utils.validators.IBanNumberValidator()], verbose_name='first shaba number'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='introducer_phone',
            field=models.CharField(max_length=12, validators=[utils.validators.PhonNumberValidator()], verbose_name='introducer phone'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='second_shaba_number',
            field=models.CharField(blank=True, max_length=36, validators=[utils.validators.IBanNumberValidator()], verbose_name='second shaba number'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='store_phone',
            field=models.CharField(max_length=12, validators=[utils.validators.PhonNumberValidator()], verbose_name='store phone'),
        ),
    ]

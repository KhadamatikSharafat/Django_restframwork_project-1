# Generated by Django 3.2 on 2022-11-22 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poses', '0013_auto_20221122_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posregister',
            name='parent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posregister', to=settings.AUTH_USER_MODEL, to_field='national_code', verbose_name='parent'),
        ),
    ]

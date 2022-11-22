# Generated by Django 3.2 on 2022-11-22 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poses', '0021_auto_20221122_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posregister',
            name='parent',
        ),
        migrations.AddField(
            model_name='posregister',
            name='user',
            field=models.ForeignKey(blank=True, default=12, on_delete=django.db.models.deletion.CASCADE, related_name='posregister', to='users.user', to_field='national_code', verbose_name='کاربر درخواست کننده'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posregister',
            name='leaseterm',
            field=models.FileField(blank=True, upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='leaseterm'),
        ),
    ]

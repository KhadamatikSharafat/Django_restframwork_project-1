# Generated by Django 3.2 on 2022-11-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0019_alter_posregister_leaseterm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posregister',
            name='leaseterm',
            field=models.FileField(blank=True, upload_to='posregister/user_<built-in function id>/%Y/%m/%d/%M/', verbose_name='leaseterm'),
        ),
    ]
# Generated by Django 3.2 on 2022-11-22 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0024_alter_posregister_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='posregister',
            table='posdocuments',
        ),
    ]
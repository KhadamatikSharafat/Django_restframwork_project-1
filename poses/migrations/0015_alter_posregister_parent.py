# Generated by Django 3.2 on 2022-11-07 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0014_alter_posregister_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posregister',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posregisters', to='poses.user', to_field='national_code', verbose_name='parent'),
        ),
    ]

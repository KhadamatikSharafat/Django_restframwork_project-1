# Generated by Django 3.2 on 2022-11-21 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0011_remove_posregister_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_code', models.CharField(max_length=10, unique=True, verbose_name='national code')),
                ('password', models.CharField(max_length=30, verbose_name='password')),
            ],
            options={
                'verbose_name': 'parent',
                'verbose_name_plural': 'parents',
                'db_table': 'parent',
            },
        ),
        migrations.AddField(
            model_name='posregister',
            name='parent',
            field=models.ForeignKey(blank=True, default=15, on_delete=django.db.models.deletion.CASCADE, related_name='posregisters', to='poses.parent', to_field='national_code', verbose_name='parent'),
            preserve_default=False,
        ),
    ]

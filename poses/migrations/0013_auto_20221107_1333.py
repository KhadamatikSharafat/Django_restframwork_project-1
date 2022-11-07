# Generated by Django 3.2 on 2022-11-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0012_alter_posregister_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posregister',
            old_name='birthday',
            new_name='birth',
        ),
        migrations.RenameField(
            model_name='posregister',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='posregister',
            old_name='State',
            new_name='state',
        ),
        migrations.AddField(
            model_name='posregister',
            name='status',
            field=models.CharField(blank=True, choices=[('ایران زمین', 'نوع ایران زمین'), ('آینده', 'نوع آینده'), ('پست بانک', 'نوع پست بانک'), ('خاورمیانه', 'نوع خاورمیانه'), ('دی', 'نوع دی'), ('رفاه', 'نوع رفاه'), ('سامان', 'نوع سامان'), ('شهر', 'نوع شهر'), ('صادرات', 'نوع صادرات'), ('کشاورزی', 'نوع کشاورزی'), ('گردشگری', 'نوع گردشگری'), ('مسکن', 'نوع مسکن'), ('ملی', 'نوع ملی'), ('اقتصاد نوین', 'نوع اقتصاد نوین'), ('پارسیان', 'نوع پارسیان'), ('تجارت', 'نوع تجارت'), ('توسعه تعاون', 'نوع توسعه تعاون'), ('سپه', 'نوع سپه'), ('سرمایه', 'نوع سرمایه'), ('سینا', 'نوع سینا'), ('صنعت و معدن', 'صنعت و معدن'), ('کار آفرین', 'کار آفرین')], default='در انتظار بررسی', max_length=60, verbose_name='status'),
        ),
    ]
# Generated by Django 3.2 on 2022-12-05 04:55

from django.db import migrations, models
import poses.models


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0003_rename_front_nationalcard_cheque_cheque_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheque',
            name='cheque_document',
            field=models.FileField(max_length=59999, upload_to=poses.models.Cheque.get_media_file_name, verbose_name='تصویر رو کارت ملی'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='first_bank_name',
            field=models.CharField(choices=[('ایران زمین', 'نوع ایران زمین'), ('آینده', 'نوع آینده'), ('پست بانک', 'نوع پست بانک'), ('خاورمیانه', 'نوع خاورمیانه'), ('دی', 'نوع دی'), ('رفاه', 'نوع رفاه'), ('سامان', 'نوع سامان'), ('شهر', 'نوع شهر'), ('صادرات', 'نوع صادرات'), ('کشاورزی', 'نوع کشاورزی'), ('گردشگری', 'نوع گردشگری'), ('مسکن', 'نوع مسکن'), ('ملی', 'نوع ملی'), ('اقتصاد نوین', 'نوع اقتصاد نوین'), ('پارسیان', 'نوع پارسیان'), ('تجارت', 'نوع تجارت'), ('توسعه تعاون', 'نوع توسعه تعاون'), ('سپه', 'نوع سپه'), ('سرمایه', 'نوع سرمایه'), ('سینا', 'نوع سینا'), ('صنعت و معدن', 'صنعت و معدن'), ('کار آفرین', 'کار آفرین')], default='ایران زمین', max_length=50, verbose_name='نام بانک '),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='psp',
            field=models.CharField(choices=[('پرداخت نوين آرين', 'پرداخت نوين آرين'), ('سابين سامان', 'سابين سامان'), ('سابين پارسيان', 'سابين پارسيان'), ('پرداخت سپهر صادرات', 'پرداخت سپهر صادرات'), ('فن آوا كارت', 'فن آوا كارت')], default='پرداخت نوين آرين', max_length=50, verbose_name='psp'),
        ),
    ]
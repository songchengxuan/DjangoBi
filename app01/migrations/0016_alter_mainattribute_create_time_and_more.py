# Generated by Django 4.1.2 on 2023-03-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_alter_datefeature_holiday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainattribute',
            name='create_time',
            field=models.DateTimeField(default='2023-03-27 16:33:32', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='mainattribute',
            name='modify_time',
            field=models.DateTimeField(default='2023-03-27 16:33:32', verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='storecomparable',
            name='create_time',
            field=models.DateTimeField(default='2023-03-27 16:33:32', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='storecomparable',
            name='modify_time',
            field=models.DateTimeField(default='2023-03-27 16:33:32', verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='storemapping',
            name='create_time',
            field=models.DateTimeField(default='2023-03-27 16:33:32', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='storemapping',
            name='modify_time',
            field=models.DateTimeField(default='2023-03-27 16:33:32', verbose_name='修改时间'),
        ),
    ]

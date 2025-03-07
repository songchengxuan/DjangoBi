# Generated by Django 4.1.2 on 2023-03-22 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_datefeature_alter_mainattribute_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datefeature',
            name='holiday',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='节假日'),
        ),
        migrations.AlterField(
            model_name='datefeature',
            name='promotion_event',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='促销活动'),
        ),
        migrations.AlterField(
            model_name='datefeature',
            name='promotion_level',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='活动等级'),
        ),
        migrations.AlterField(
            model_name='mainattribute',
            name='create_time',
            field=models.DateTimeField(default='2023-03-22 09:53:47', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='mainattribute',
            name='modify_time',
            field=models.DateTimeField(default='2023-03-22 09:53:47', verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='storecomparable',
            name='create_time',
            field=models.DateTimeField(default='2023-03-22 09:53:47', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='storecomparable',
            name='modify_time',
            field=models.DateTimeField(default='2023-03-22 09:53:47', verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='storemapping',
            name='create_time',
            field=models.DateTimeField(default='2023-03-22 09:53:47', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='storemapping',
            name='modify_time',
            field=models.DateTimeField(default='2023-03-22 09:53:47', verbose_name='修改时间'),
        ),
    ]

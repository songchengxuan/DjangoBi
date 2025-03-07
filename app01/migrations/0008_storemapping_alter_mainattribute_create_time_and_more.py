# Generated by Django 4.1.2 on 2023-03-10 09:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_delete_regionmession_alter_mainattribute_create_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_store_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)], verbose_name='老门店ID')),
                ('new_store_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)], verbose_name='新门店ID')),
                ('new_branch_id', models.CharField(max_length=10, verbose_name='新连锁公司ID')),
                ('create_time', models.DateTimeField(default='2023-03-10 17:15:56', verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(default='2023-03-10 17:15:56', verbose_name='修改时间')),
            ],
        ),
        migrations.AlterField(
            model_name='mainattribute',
            name='create_time',
            field=models.DateTimeField(default='2023-03-10 17:15:56', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='mainattribute',
            name='modify_time',
            field=models.DateTimeField(default='2023-03-10 17:15:56', verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='storecomparable',
            name='create_time',
            field=models.DateTimeField(default='2023-03-10 17:15:56', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='storecomparable',
            name='modify_time',
            field=models.DateTimeField(default='2023-03-10 17:15:56', verbose_name='修改时间'),
        ),
    ]

# Generated by Django 4.1.2 on 2023-05-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_alter_mission_create_time_alter_mission_start_sdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='create_time',
            field=models.DateTimeField(default='2023-05-04 08:52:11', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='start_sdate',
            field=models.DateField(default='2023-05-04 08:52:11', verbose_name='预测开始时间'),
        ),
        migrations.AlterField(
            model_name='predresult',
            name='create_time',
            field=models.DateTimeField(default='2023-05-04 08:52:11', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='predresult',
            name='modify_time',
            field=models.DateTimeField(default='2023-05-04 08:52:11', verbose_name='修改时间'),
        ),
    ]

# Generated by Django 4.1.2 on 2023-03-31 09:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads0202',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdate', models.DateField(verbose_name='日期')),
                ('branch_id', models.CharField(max_length=40, verbose_name='连锁公司ID')),
                ('branch_name', models.CharField(max_length=120, verbose_name='连锁公司')),
                ('org_org_department_id', models.CharField(blank=True, max_length=120, null=True, verbose_name='营业部ID')),
                ('org_department_name', models.CharField(blank=True, max_length=120, null=True, verbose_name='营业部')),
                ('org_operational_region_id', models.CharField(blank=True, max_length=120, null=True, verbose_name='营业大区ID')),
                ('operational_region_desc', models.CharField(blank=True, max_length=250, null=True, verbose_name='营业大区')),
                ('store_id', models.CharField(blank=True, max_length=40, null=True, verbose_name='门店ID')),
                ('store_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='门店名称')),
                ('zzdalei_desc', models.CharField(blank=True, max_length=120, null=True, verbose_name='大类名称')),
                ('zzzhonglei_desc', models.CharField(blank=True, max_length=120, null=True, verbose_name='中类名称')),
                ('xiaolei_desc', models.CharField(blank=True, max_length=120, null=True, verbose_name='小类名称')),
                ('main_attribute', models.CharField(blank=True, max_length=250, null=True, verbose_name='主推属性')),
                ('satnr', models.CharField(blank=True, max_length=120, null=True, verbose_name='款')),
                ('skc', models.CharField(blank=True, max_length=250, null=True, verbose_name='skc')),
                ('business_amount', models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='营业额')),
                ('business_qty', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)], verbose_name='销量')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='数据集名称')),
                ('business_class', models.CharField(max_length=120, verbose_name='度量类型')),
                ('class_dim', models.CharField(max_length=120, verbose_name='品类维度')),
                ('class_value', models.CharField(max_length=120, verbose_name='品类维度值')),
                ('region_dim', models.CharField(max_length=120, verbose_name='组织维度')),
                ('region_value', models.CharField(max_length=120, verbose_name='组织维度值')),
                ('time_scale', models.CharField(max_length=40, verbose_name='输出时间尺度')),
                ('start_sdate', models.DateField(default='2023-03-31 09:06:53', verbose_name='预测开始时间')),
                ('daterange', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)], verbose_name='预测区间')),
                ('remark', models.CharField(default='已提交', max_length=40, verbose_name='任务状态')),
                ('error', models.FloatField(default=0, verbose_name='预测误差')),
                ('create_time', models.DateTimeField(default='2023-03-31 09:06:53', verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='PredResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='数据集名称')),
                ('pid', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)], verbose_name='任务ID')),
                ('error', models.FloatField(verbose_name='误差')),
                ('pred_value', models.FloatField(verbose_name='预测值')),
                ('actual_value', models.FloatField(verbose_name='实际值')),
                ('lower_bound', models.FloatField(verbose_name='下限')),
                ('upper_bound', models.FloatField(verbose_name='上限')),
                ('create_time', models.DateTimeField(default='2023-03-31 09:06:53', verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(default='2023-03-31 09:06:53', verbose_name='修改时间')),
            ],
        ),
    ]

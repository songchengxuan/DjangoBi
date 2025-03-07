from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.
class PredResult(models.Model):
    """ 预测结果表 """
    name = models.CharField(verbose_name="数据集名称", max_length=250)
    pid = models.IntegerField(verbose_name="任务ID", validators=[MinValueValidator(1), MaxValueValidator(8)])
    error = models.FloatField(verbose_name="误差")
    pred_value = models.FloatField(verbose_name="预测值")
    actual_value = models.FloatField(verbose_name="实际值")
    lower_bound = models.FloatField(verbose_name="下限")
    upper_bound = models.FloatField(verbose_name="上限")
    create_time = models.DateTimeField(verbose_name="创建时间", default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    modify_time = models.DateTimeField(verbose_name="修改时间", default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class Mission(models.Model):
    """ 时序预测任务表 """
    name = models.CharField(verbose_name="数据集名称", max_length=250)
    business_class = models.CharField(verbose_name="度量类型", max_length=120)
    class_dim = models.CharField(verbose_name="品类维度", max_length=120)
    class_value = models.CharField(verbose_name="品类维度值", max_length=120)
    region_dim = models.CharField(verbose_name="组织维度", max_length=120)
    region_value = models.CharField(verbose_name="组织维度值", max_length=120)
    time_scale = models.CharField(verbose_name="输出时间尺度", max_length=40)
    start_sdate = models.DateField(verbose_name="预测开始时间", default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    daterange = models.IntegerField(verbose_name="预测区间",  validators=[MinValueValidator(1), MaxValueValidator(8)])
    remark = models.CharField(verbose_name="任务状态", max_length=40, default="已提交")
    error = models.FloatField(verbose_name="预测误差", default=0)
    create_time = models.DateTimeField(verbose_name="创建时间", default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class Ads0202(models.Model):
    """ 0202.1抽取表，保留近两年数据 """
    sdate = models.DateField(verbose_name="日期")
    branch_id = models.CharField(verbose_name="连锁公司ID", max_length=40)
    branch_name = models.CharField(verbose_name="连锁公司", max_length=120)
    org_org_department_id = models.CharField(verbose_name="营业部ID", max_length=120, null=True, blank=True)
    org_department_name = models.CharField(verbose_name="营业部", max_length=120, null=True, blank=True)
    org_operational_region_id = models.CharField(verbose_name="营业大区ID", max_length=120, null=True, blank=True)
    operational_region_desc = models.CharField(verbose_name="营业大区", max_length=250, null=True, blank=True)
    store_id = models.CharField(verbose_name="门店ID", max_length=40, null=True, blank=True)
    store_name = models.CharField(verbose_name="门店名称", max_length=250, null=True, blank=True)
    zzdalei_desc = models.CharField(verbose_name="大类名称", max_length=120, null=True, blank=True)
    zzzhonglei_desc = models.CharField(verbose_name="中类名称", max_length=120, null=True, blank=True)
    xiaolei_desc = models.CharField(verbose_name="小类名称", max_length=120, null=True, blank=True)
    main_attribute = models.CharField(verbose_name="主推属性", max_length=250, null=True, blank=True)
    satnr = models.CharField(verbose_name="款", max_length=120, null=True, blank=True)
    skc = models.CharField(verbose_name="skc", max_length=250, null=True, blank=True)
    business_amount = models.DecimalField(verbose_name="营业额", max_digits=12, decimal_places=2, null=True)
    business_qty = models.IntegerField(verbose_name="销量", validators=[MinValueValidator(1), MaxValueValidator(8)], null=True)

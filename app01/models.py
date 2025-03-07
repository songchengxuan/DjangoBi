from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.
class MainAttribute(models.Model):
    """ Y1.主推商品属性表 """
    branch_id = models.CharField(verbose_name="连锁公司ID", max_length=80)
    satnr = models.CharField(verbose_name="商品代码", max_length=80)
    main_attribute = models.CharField(verbose_name="主推名称", max_length=120)
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    modify_time = models.DateTimeField(verbose_name="修改时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class StoreComparable(models.Model):
    """ Y2.可比门店表 """
    store_id = models.IntegerField(verbose_name="门店ID", validators=[MinValueValidator(1), MaxValueValidator(8)])
    is_comparable = models.CharField(verbose_name="是否可比店", max_length=10)
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    modify_time = models.DateTimeField(verbose_name="修改时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class StoreMapping(models.Model):
    """ Y3.新老门店映射表 """
    old_store_id = models.IntegerField(verbose_name="老门店ID", validators=[MinValueValidator(1), MaxValueValidator(8)])
    new_store_id = models.IntegerField(verbose_name="新门店ID", validators=[MinValueValidator(1), MaxValueValidator(8)])
    new_branch_id = models.CharField(verbose_name="新连锁公司ID", max_length=10)
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    modify_time = models.DateTimeField(verbose_name="修改时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class DateFeature(models.Model):
    """ 日期特征表 """
    sdate = models.DateField(verbose_name="日期")
    holiday = models.CharField(verbose_name="节假日", max_length=40, null=True, blank=True)
    promotion_event = models.CharField(verbose_name="促销活动", max_length=80, null=True, blank=True)
    promotion_level = models.CharField(verbose_name="活动等级", max_length=10, null=True, blank=True)

class StoreAssign(models.Model):
    """ Y4.加盟商结算指定门店下发表 """
    store_id = models.IntegerField(verbose_name="门店ID", validators=[MinValueValidator(1), MaxValueValidator(8)])
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    modify_time = models.DateTimeField(verbose_name="修改时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


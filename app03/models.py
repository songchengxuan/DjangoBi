from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime

# Create your models here.
class ChannelSales(models.Model):
    """ 左1.全渠道销售汇总 """
    # 渠道、金额
    channel = models.CharField(verbose_name="渠道", max_length=40)
    business_amount = models.FloatField(verbose_name="营业额")
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class BranchSales(models.Model):
    """ 左2.连锁公司营业额 """
    # 连锁公司、日期（月日）、金额
    branch_name = models.CharField(verbose_name="连锁公司", max_length=40)
    sdate_md = models.CharField(verbose_name="日期（月日）", max_length=20)
    business_amount = models.FloatField(verbose_name="营业额")
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class TypeSales(models.Model):
    """ 左3.品类营业额 """
    # 自定义大类、营业额、同期营业额、毛利率
    classification_dalei_desc = models.CharField(verbose_name="自定义大类", max_length=80)
    business_amount = models.FloatField(verbose_name="营业额")
    business_amount_corr = models.FloatField(verbose_name="同期营业额")
    business_profit = models.FloatField(verbose_name="毛利率")
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class ProvinceSales(models.Model):
    """ 中1.省份营业额 """
    # 省份、年份、营业额
    province_name = models.CharField(verbose_name="省份", max_length=120)
    year_desc = models.CharField(verbose_name="年份", max_length=20)
    business_amount = models.FloatField(verbose_name="营业额")
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class VipNums(models.Model):
    """ 中2.会员人数 """
    # 会员等级、人数
    grade_name = models.CharField(verbose_name="会员等级", max_length=80)
    business_amount = models.FloatField(verbose_name="营业额")
    total_vip_num = models.IntegerField(verbose_name="人数", validators=[MinValueValidator(1), MaxValueValidator(8)],
                                       null=True)
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class StoreTop(models.Model):
    """ 右1.门店销售排行top10 """
    # 门店名称、营业额，昨日
    store_name = models.CharField(verbose_name="门店名称", max_length=240)
    business_amount = models.FloatField(verbose_name="营业额")
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class OrderDtl(models.Model):
    """ 右2.下单信息表 """
    # 会员名称、门店名称、自定义中分类，金额，昨日，挑30个出来
    store_name = models.CharField(verbose_name="门店名称", max_length=240)
    vip_name = models.CharField(verbose_name="会员名称", max_length=240)
    classification_zhonglei_desc = models.CharField(verbose_name="自定义中分类", max_length=240)
    business_amount = models.FloatField(verbose_name="营业额")
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

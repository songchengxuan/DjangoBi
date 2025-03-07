import pandas as pd
import datetime
import time
from datetime import timedelta

#======公用函数========
# 日期转字符串函数
def int_to_date(para):
    if len(para) <= 5:
        delta = pd.Timedelta(str(para)+'days')
        time = pd.to_datetime('1899-12-30') + delta
    else:
        time = para
    return time

# 日期增加N天 或减少N天
def date_add(date_str, add_count=1):
    """
    date_str为初始日期，例如：2019-01-01
    add_count为增减天数，例如 -2 表示减两天
    """
    date_list = time.strptime(date_str, "%Y-%m-%d")
    y, m, d = date_list[:3]
    delta = timedelta(days=add_count)
    date_result = datetime.datetime(y, m, d) + delta
    date_result = date_result.strftime("%Y-%m-%d")
    return date_result
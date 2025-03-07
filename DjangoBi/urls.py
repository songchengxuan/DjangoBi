from django.urls import path
from app01 import views as views01
from app02 import views as views02
from app03 import views as views03

urlpatterns = [
    # project name: app01
    # create info: 2022-10-31 by scx
    path('index/', views01.index),
    # Y1.主推商品属性表
    path('y1/list/', views01.y1_list),
    path('y1/add/', views01.y1_add),
    path('y1/delete/', views01.y1_delete),
    path('y1/upload/', views01.y1_upload),
    path('y1/push/', views01.y1_push),
    # Y2.可比门店表
    path('y2/list/', views01.y2_list),
    path('y2/add/', views01.y2_add),
    path('y2/delete/', views01.y2_delete),
    path('y2/upload/', views01.y2_upload),
    path('y2/push/', views01.y2_push),
    # Y3.新老门店映射表
    path('y3/list/', views01.y3_list),
    path('y3/add/', views01.y3_add),
    path('y3/delete/', views01.y3_delete),
    path('y3/upload/', views01.y3_upload),
    path('y3/push/', views01.y3_push),
    # Y4.加盟商指定门店下发表
    path('y4/list/', views01.y4_list),
    path('y4/upload/', views01.y4_upload),
    path('y4/push/', views01.y4_push),

    # project name: app02
    # create info: 2023-03-11 by scx
    path('mission/list/', views02.mission_list),
    path('mission/add/', views02.mission_add),
    path('mission/class/', views02.mission_class),
    path('mission/region/', views02.mission_region),
    path('mission/test/', views02.mission_test),

    # project name: app03
    # create info: 2023-05-26 by scx
    path('screen/l1/', views03.channel_sales_list),
    path('screen/l2/', views03.branch_sales_list),
    path('screen/l3/', views03.type_sales_list),
    path('screen/m1/', views03.province_sales_list),
    path('screen/m2/', views03.vip_nums_list),
    path('screen/r1/', views03.store_top_list),
    path('screen/r2/', views03.order_dtl_list),
]



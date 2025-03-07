from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from django.forms import model_to_dict
from app03 import models


# ====== 左1.全渠道销售汇总 ======
@require_http_methods(["GET"])
def channel_sales_list(request):
    response = {}
    try:
        # === 查询全部 ===
        queryset = models.ChannelSales.objects.all()
        response['data'] = []
        for i in queryset:
            response['data'].append(model_to_dict(i))
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

# ====== 左2.连锁公司营业额 ======
@require_http_methods(["GET"])
def branch_sales_list(request):
    response = {}
    try:
        # === 查询全部 ===
        queryset = models.BranchSales.objects.all()
        response['data'] = []
        for i in queryset:
            response['data'].append(model_to_dict(i))
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

# ====== 左3.品类营业额 ======
@require_http_methods(["GET"])
def type_sales_list(request):
    response = {}
    try:
        # === 查询全部 ===
        queryset = models.TypeSales.objects.all()
        response['data'] = []
        for i in queryset:
            response['data'].append(model_to_dict(i))
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

# ====== 中1.省份营业额 ======
@require_http_methods(["GET"])
def province_sales_list(request):
    response = {}
    try:
        # === 查询全部 ===
        queryset = models.ProvinceSales.objects.all()
        response['data'] = []
        for i in queryset:
            response['data'].append(model_to_dict(i))
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

# ====== 中2.会员人数 ======
@require_http_methods(["GET"])
def vip_nums_list(request):
    response = {}
    try:
        # === 查询全部 ===
        queryset = models.VipNums.objects.all()
        response['data'] = []
        for i in queryset:
            response['data'].append(model_to_dict(i))
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

# ====== 右1.门店销售排行top10 ======
@require_http_methods(["GET"])
def store_top_list(request):
    response = {}
    try:
        # === 查询全部 ===
        queryset = models.StoreTop.objects.all()
        response['data'] = []
        for i in queryset:
            response['data'].append(model_to_dict(i))
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

# ====== 右2.下单信息表 ======
@require_http_methods(["GET"])
def order_dtl_list(request):
    response = {}
    try:
        # === 查询全部 ===
        queryset = models.OrderDtl.objects.all()
        response['data'] = []
        for i in queryset:
            response['data'].append(model_to_dict(i))
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)
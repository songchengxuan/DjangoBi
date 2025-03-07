from django.db.models import F, Max
from django.forms import model_to_dict
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from app02 import models
from app02 import pred


def index(request):
    return HttpResponse("欢迎使用")


# ======时序预测任务表=======
# 按ID查询
@require_http_methods(["GET"])
def mission_list(request):
    """ list列表 + 查找数据(模糊查询) """
    response = {}
    try:
        # === 查询开始 ===
        data_dict = {}
        id = request.GET.get('id')
        if id:
            data_dict["id__contains"] = id
        # === 查询结束 ===
        queryset = models.Mission.objects.filter(**data_dict)
        response['data'] = []
        for i in queryset:
            response['data'].append(model_to_dict(i))
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def mission_add(request):
    """ list列表添加与编辑 """
    response = {}
    try:
        # === 开始 ===
        nid = request.GET.get('id')
        data_dict = {
            "name": request.GET.get('name'),
            "business_class": request.GET.get('business_class'),
            "class_dim": request.GET.get('class_dim'),
            "class_value": request.GET.get('class_value'),
            "region_dim": request.GET.get('region_dim'),
            "region_value": request.GET.get('region_value'),
            "time_scale": request.GET.get('time_scale'),
            "start_sdate": request.GET.get('start_sdate'),
            "daterange": request.GET.get('daterange'),
            "remark": "已提交"
        }
        # === 算法传参 ===
        random_forest = pred.RandomForest(data_dict)
        res, error = random_forest.random_forest()
        data_dict["error"] = error
        if nid:
            models.Mission.objects.filter(id=nid).update(**data_dict)
        else:
            models.Mission.objects.create(**data_dict)
        # === 算法结果存储 ===
        for row in res.itertuples():
            models.PredResult.object.create(name=row.name,
                                            std=row.std,
                                            pred_value=row.pred_value,
                                            actual_value=row.actual_value,
                                            lower_bound=row.lower_bound,
                                            upper_bound=row.upper_bound,
                                            create_time=row.create_time,
                                            modify_time=row.modify_time)
        # === 结束 ===
        response['msg'] = 'success'
        # === 算法传参 ===
        random_forest(data_dict)
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def mission_class(request):
    """ 查询品类维度值 """
    response = {}
    try:
        # === 查询开始 ===
        class_dim = request.GET.get('class_dim')
        if class_dim == 'zzdalei_desc':
            queryset = models.Ads0202.objects.filter(zzdalei_desc__isnull=False) \
                .annotate(class_value=F('zzdalei_desc'), ).values('class_value').distinct()
        elif class_dim == 'zzzhonglei_desc':
            queryset = models.Ads0202.objects.filter(zzzhonglei_desc__isnull=False) \
                .annotate(class_value=F('zzzhonglei_desc'), ).values('class_value').distinct()
        elif class_dim == 'xiaolei_desc':
            queryset = models.Ads0202.objects.filter(xiaolei_desc__isnull=False) \
                .annotate(class_value=F('xiaolei_desc'), ).values('class_value').distinct()
        response['data'] = []
        for i in queryset:
            response['data'] = list(queryset)
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def mission_region(request):
    """ 查询组织维度值 """
    response = {}
    try:
        # === 查询开始 ===
        region_dim = request.GET.get('region_dim')
        if region_dim == 'branch_id':
            queryset = models.Ads0202.objects.filter(branch_id__isnull=False) \
                .annotate(region_value=F('branch_id'), ).values('region_value').distinct()
        elif region_dim == 'org_org_department_id':
            queryset = models.Ads0202.objects.filter(org_org_department_id__isnull=False) \
                .annotate(region_value=F('org_org_department_id'), ).values('region_value').distinct()
        elif region_dim == 'org_operational_region_id':
            queryset = models.Ads0202.objects.filter(org_operational_region_id__isnull=False) \
                .annotate(region_value=F('org_operational_region_id'), ).values('region_value').distinct()
        response['data'] = []
        for i in queryset:
            response['data'] = list(queryset)
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def mission_test(request):
    """ list列表添加与编辑 """
    response = {}
    data_dict = {
        "name": '0202',
        "business_class": 'business_amount',
        "class_dim": 'classification_dalei_desc',
        "class_value": '衬衫',
        "region_dim": 'branch_id',
        "region_value": 'DC13',
        "time_scale": 'days',
        "start_sdate": '2023-03-15',
        "daterange": '3',
        "remark": "已提交"
    }
    # === 算法传参 ===
    random_forest = pred.RandomForest(data_dict)
    df, error = random_forest.random_forest()
    data_dict["error"] = error
    models.Mission.objects.create(**data_dict)
    # === 算法结果存储 ===
    pid = models.Mission.objects.all().aggregate(Max('id'))['id__max']
    for row in df.itertuples():
        models.PredResult.objects.create(name=row.name,
                                         pid=pid,
                                         error=row.error,
                                         pred_value=row.pred_value,
                                         actual_value=row.actual_value,
                                         lower_bound=row.lower_bound,
                                         upper_bound=row.upper_bound,
                                         create_time=row.create_time,
                                         modify_time=row.modify_time)
    # === 结束 ===
    response['msg'] = 'success'
    return JsonResponse(response)

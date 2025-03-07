from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
import psycopg2
from DjangoBi.gplink import gp_connect
from DjangoBi.public import date_add
import pandas as pd
import numpy as np

class RandomForest:
    # 解析参数
    def __init__(self, params):
        self.name = params['name']
        self.business_class = params['business_class']
        self.class_dim = params['class_dim']
        self.class_value = params['class_value']
        self.region_dim = params['region_dim']
        self.region_value = params['region_value']
        self.time_scale = params['time_scale']
        self.start_sdate = params['start_sdate']
        self.daterange = params['daterange']
        self.create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    def sql_link(self):
        # 日期计算
        if (self.time_scale == 'days'):
            end_sdate = date_add(self.start_sdate, int(self.daterange))
            # SQL语句拼接
            sql = """
                with sale as (
                select 
                    sdate
                    ,branch_id
                    ,round(sum(business_qty),0) as business
                from ads.ads_sales_source_store_skc_day
                where zzzhonglei_desc = '衬衫' and sdate >= '2021-01-01'
                group by sdate ,branch_id)
                select 
                    t1.sdate
                    ,t1.business
                    ,t2.business_corr 
                    ,case when df.holiday is null then 0 
                        else 1 end as holiday
                    ,case when df.promotion_event is null then 0 
                        else 1 end as promotion_event
                    ,case when df.promotion_level = 'A-' then 1
                        when df.promotion_level = 'A' then 2
                        when df.promotion_level = 'S' then 3
                        else 0 end as promotion_level
                from 
                    sale t1
                left join 
                    (select 
                        sdate + interval '1 year' as sdate
                        ,branch_id 
                        ,business as business_corr
                    from sale) t2
                    on t1.sdate = t2.sdate
                inner join ods.ods_ext_datefeature df
                    on t1.sdate = df.sdate 
                    and t1.branch_id = df.branch_id 
                where t1.sdate >= '2022-01-01'
                order by t1.sdate desc
                """
        return sql
    # 数据获取
    def get_data(self):
        # 开始查询
        sql = self.sql_link()
        conn = gp_connect()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(sql)
        res = cur.fetchall()
        # 将获得的列名元组数据转换为dataframe
        col = [item[0] for item in cur.description]
        df = pd.DataFrame(res, columns=col)
        conn.commit()
        conn.close()
        return res, df
    # 算法执行
    def random_forest(self):
        # 参数配置
        pd.set_option('display.unicode.east_asian_width', True)  # 列名与值对齐
        pd.set_option('display.max_columns', None)  # 设置None则无列数的显示限制
        pd.set_option('display.width', 1000)  # 不换行显示
        res, data_org = self.get_data()
        print(data_org.head(3))
        # 预测用数据
        data_train = data_org[data_org['sdate'] < datetime.strptime("2023-03-19", '%Y-%m-%d').date()]
        data_test = data_org[(data_org['sdate'] >= datetime.strptime("2023-03-19", '%Y-%m-%d').date()) & (data_org['sdate'] <= datetime.strptime("2023-03-23", '%Y-%m-%d').date())]
        x_train = np.array(data_train[["holiday", "promotion_event", "promotion_level", "business_corr"]])
        y_train = np.array(data_train[["business"]]).astype(np.float).reshape(-1)
        x_test = np.array(data_test[["holiday", "promotion_event", "promotion_level", "business_corr"]])
        y_test = np.array(data_test[["business"]]).astype(np.float).reshape(-1)
        # 输出数据
        data_actual = data_org[(data_org['sdate'] >= datetime.strptime("2023-03-19", '%Y-%m-%d').date()) & (data_org['sdate'] <= datetime.strptime("2023-03-23", '%Y-%m-%d').date())]
        y_actual = np.array(data_actual[["business"]])
        days_pred = np.array(data_actual["sdate"].apply(lambda x: x.strftime("%Y-%m-%d")))
        # 预测和绘图
        regr = RandomForestRegressor(criterion='squared_error',
                                     # 衡量回归效果的指标,可选项有squared_error, absolute_error, friedman_mse, poisson
                                     max_depth=5,
                                     # 数值型，默认值None。这是与剪枝相关的参数，设置为None时，树的节点会一直分裂，直到：（1）每个叶子都是“纯”的；（2）或者叶子中包含于min_sanples_split个样本。推荐从 max_depth = 3 尝试增加，观察是否应该继续加大深度。
                                     min_samples_split=2,
                                     # 数值型，默认值2，指定每个内部节点(非叶子节点)包含的最少的样本数。与min_samples_leaf这个参数类似，可以是整数也可以是浮点数。
                                     min_samples_leaf=1,
                                     # 数值型，默认值1，指定每个叶子结点包含的最少的样本数。参数的取值除了整数之外，还可以是浮点数，此时（min_samples_leaf * n_samples）向下取整后的整数是每个节点的最小样本数。此参数设置的过小会导致过拟合，反之就会欠拟合。
                                     min_impurity_decrease=1e-07,
                                     # float, optional (default=0.)如果节点的分裂导致不纯度的减少(分裂后样本比分裂前更加纯净)大于或等于min_impurity_decrease，则分裂该节点。
                                     verbose=0,  # (default=0) 是否显示任务进程
                                     warm_start=False)  # 热启动，决定是否使用上次调用该类的结果然后增加新的。
        regr.fit(x_train, y_train)
        print("Traing Score:%f" % regr.score(x_train, y_train))
        print("Testing Score:%f" % regr.score(x_test, y_test))
        y_pred = regr.predict(x_test)
        # TTL_FA
        APE = []
        for day in range(5):
            per_err = (y_pred[day] - y_test[day])
            APE.append(per_err)
        error = 1 - abs(sum(APE)) / sum(y_test)
        print("预测准确度：", error)
        # 置信区间,置信水平和Z值对应：90%-1.64,95%-1.96,99%-2.58
        std = float(y_train.std())
        lower_bound = np.maximum(y_pred - 1.5 * std, 0)
        upper_bound = np.minimum(y_pred + 1.5 * std, max(y_train))
        # 存入预测结果,预测字段为name,sdate,std,pred_value,actual_value,lower_bound,upper_bound,create_time,modify_time
        # 原表保留去年至算法日期前的数据,
        df_save = pd.DataFrame(columns=['name', 'error', 'pred_value', 'actual_value', 'lower_bound', 'upper_bound', 'create_time', 'modify_time'])
        modify_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for i in range(0, len(y_test)):
            df_save.loc[i]=[self.name, error, y_pred[i], y_test[i], lower_bound[i], upper_bound[i], self.create_time, modify_time]
        return df_save, error


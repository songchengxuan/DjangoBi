import psycopg2


def gp_connect():
    try:
        db = psycopg2.connect(dbname="hodo_dw",
                              user="etl",
                              password="Asd123123!",
                              host="10.10.67.160",
                              port="5432")
        # connect()也可以使用一个大的字符串参数,
        # 比如”host=localhost port=5432 user=postgres password=postgres dbname=test”
        return db
    except psycopg2.DatabaseError as e:
        print("could not connect to Greenplum server", e)

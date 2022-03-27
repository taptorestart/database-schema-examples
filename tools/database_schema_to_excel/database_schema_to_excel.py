import pymysql.cursors
import pandas as pd

# Database connection
username = 'username'
password = 'verysecret'
host = 'db_host'
port = 3306
database = 'db_name'

connection = pymysql.connect(host=host,
                             user=username,
                             password=password,
                             database=database,
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        sql = "show tables;"
        cursor.execute(sql, ())
        tables = cursor.fetchall()
        df_tables = pd.DataFrame(data=tables)
        
def get_tables(table_name):
    connection = pymysql.connect(host=host,
                                 user=username,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            sql = "show full columns from {};".format(table_name)
            cursor.execute(sql, ())
            columns = cursor.fetchall()
            df_columns = pd.DataFrame(data=columns)
            df_columns.insert(loc=0, column='table', value=table_name)
            df_list.append(df_columns)
            
df_list = []
tables_in = f'Tables_in_{database}'
for table_name in df_tables[tables_in].tolist():
    get_tables(table_name)
df_columns_all = pd.concat([df for df in df_list], axis=0)
df_columns_all.reset_index(drop=True, inplace=True)
df_columns_all.to_excel('./{}.xlsx'.format(database))
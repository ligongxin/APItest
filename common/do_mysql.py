#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/1017:49
#文件     :
#IDE      :PyCharm
import mysql.connector
from common import project_path
config={'host':'192.168.xx.xx',
        'user':'root',
        'password':'123456',
        'port':3306 ,
        'database':'seedit_flome',#指定你的数据库名
        }

class DoMysql:
    def do_mysql(self,sql):
        config=eval(ReadConfig().read_config(project_path.db_config_path,'DB','config'))
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        cursor.execute(sql)
        res=cursor.fetchall()
        cursor.close()
        conn.close()
        return res

# if __name__=='__main__':
    # sql='SELECT app_uid FROM `user` WHERE email="123456@qq.com"'
    # res=DoMysql().do_mysql(config,sql)
    # print(res[0][0])

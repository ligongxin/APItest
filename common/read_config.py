#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/10/916:22
#文件     :
#IDE      :PyCharm

import configparser
from common import project_path
class ReadConfig:
    def read_config(self,file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')  #打开

        #获取数据
        value=cf.get(section,option)
        return value

if __name__ == '__main__':
    file_path=project_path.db_config_path
    value=eval(ReadConfig().read_config(file_path,'DB','config'))
    print(value)
#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/10/1415:14
#文件     :
#IDE      :PyCharm
from openpyxl import load_workbook
from common import project_path

class GetInfoData:
    wb=load_workbook(project_path.test_case_path)

    login_phone=wb['info'].cell(1,2).value



if __name__ == '__main__':
    print(GetInfoData.login_phone)
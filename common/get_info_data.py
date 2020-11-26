#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/10/1415:14
#文件     :
#IDE      :PyCharm
from openpyxl import load_workbook
from common import project_path,setting
import random



class GetInfoData:
    def __init__(self):
        self.wb=load_workbook(project_path.test_case_path)

        self.login_phone=self.wb['info'].cell(1,2).value

        # product_token = wb['info'].cell(2,2).value

    def get_token(self):
        if setting.ENVIRONMENT == 3:
            token = self.wb['info'].cell(2, 2).value
        elif setting.ENVIRONMENT == 2:
            token = self.wb['info'].cell(4, 2).value
        else:
            token = self.wb['info'].cell(3, 2).value
        return token

    def get_hander(self):
        handers=[{'User-Agent':'bz-mindfulness-android-1.5.1 from android sdk version:24 mobile versionCode:7.0 phone model:PRO 7-H BZChannelNo-baidu',
        'Content-Type':'application/x-www-form-urlencoded'},
                 {'User-Agent':'bz-mindfulness-android-1.5.1 from android sdk version:28 mobile versionCode:9 phone model:MI 8 Lite BZChannelNo-xiaomib'},
                 ]
        return random.choice(handers)

    def BaseUrl(self,num=None):
        if num==3:
            base_url = 'bozhong.com'
        elif num==2:
            base_url = 'online.seedit.cc'
        else:
            base_url = 'office.bzdev.net'
        return base_url



#环境切换
def Application_profiles(data):
    res_data=[]
    for item in data:
        item['url'] = item['url'].replace('office.bzdev.net', GetInfoData().BaseUrl(setting.ENVIRONMENT))
        res_data.append(item)
    return res_data


if __name__ == '__main__':
    # print(type(GetInfoData.base_url))
    # print(GetInfoData().BaseUrl(setting.ENVIRONMENT))
    print(GetInfoData().login_phone)
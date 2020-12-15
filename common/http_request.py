#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/814:22
#文件     :
#IDE      :PyCharm
import time

import requests,json

OKGREEN = '\033[32m'
ERROR = '\033[31m'
WARNING = '\033[33m'
END = '\033[0m'
header={'User-Agent':'bz-mindfulness-android-1.5.1 from android sdk version:24 mobile versionCode:7.0 phone model:PRO 7-H BZChannelNo-baidu',
        'Content-Type':'application/x-www-form-urlencoded'}
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from common.my_log import MyLog

logger=MyLog()

class HttpRequtser:

    def http_request(self,url,param,http_method,**kwargs):

        if http_method.upper()=='POST':
            try:
                res=requests.post(url,param,**kwargs)
                print(OKGREEN+'正在进行post请求 ')
                logger.info('正在进行post请求 ')
            except Exception as e:
                print("post请求出现了异常:{0}".format(e))
                logger.error("post请求出现了异常:{0}".format(e))
        elif http_method.upper()=='PUT':
            try:
                res=requests.put(url,param,**kwargs)
                print('正在进行PUT请求 ')
                logger.info('正在进行PUT请求 ')
            except Exception as e:
                print("PUT请求出现了异常:{0}".format(e))
                logger.error("PUT请求出现了异常:{0}".format(e))

        elif http_method.upper()=='DELETE':
            try:
                res = requests.delete(url,params=param,**kwargs)
                print('正在进行DELETE请求 ')
                logger.info('正在进行DELETE请求 ')
            except Exception as e:
                print("DELETE请求出现了异常:{0}".format(e))
                logger.error("DELETE请求出现了异常:{0}".format(e))

        else:
            try:
                res=requests.get(url,param,**kwargs)
                print(OKGREEN+'正在进行get请求 ')
                logger.info(OKGREEN+'正在进行get请求 ')
            except Exception as e:
                print("get请求出现了异常:{0}".format(e))
                logger.error("get请求出现了异常:{0}".format(e))

        # access_token=res['data']['access_token']
        # print("http请求的结果是:{0}".format(access_token))
        return res

if __name__=='__main__':
    re1=HttpRequtser()
    # import time
    # url='https://account.office.bzdev.net/restful/register/getappmobilecaptcha.json'
    # data={'captcha_type':'member_register','captcha_count':1,'phone_prefix':86,'mobile':13200000004}
    # r=re1.http_request(url,data,'post',verify=False,headers=header)
    # # r = requests.post(url, data, 'post', verify=False,headers=header)
    # print(r.json())
    # code=r.json()['data']['idstring']
    #
    # time.sleep(1)
    # url = 'https://account.office.bzdev.net/restful/app/codelogin.json'
    # data = {'is_debug': 0, 'mobilecaptcha':code, 'phone_prefix': 86, 'phone': 13200000004,'type':1}
    #
    # lo=re1.http_request(url,data,'post',verify=False,headers=header)
    # print(lo.json())
    # token=None
    # if lo.json()['data']['access_token']:
    #     # header['access_token']=tokin
    #     token = lo.json()['data']['access_token']
    #     print(111)
    # print(header)
    # time.sleep(1)
    #
    # url = 'https://api.office.bzdev.net/mindfulness/restful/member/profile.json'
    # data={'access_token':token}
    # pro=re1.http_request(url,data,'get',headers=header,verify=False)
    # print(pro.json())

    # url='http://api.mindfulness.office.bzdev.net/mindfulness/restful/home/follow.json'
    # for i in range(1,10000):
    #     app_uid=310000+i
    #     data={'access_token':'88e613d776dc5db771b4bb418d96086d','seedit_signature':'q5Hrl7DwmLVPpTBPQu7SpWWSa6J8csCgG9Eqit4Le35szdhJo4d27JqwLynkpQ/ONx33gwdUmJeaJ2XX8vJX3A==','type':0,'app_uid':app_uid}
    #     res=re1.http_request(url,data,'post',headers=header,verify=False)
    #     print(res.json())
        # time.sleep()
    from common.do_excel import DoExce
    from common import project_path
    data = DoExce(project_path.test_case_path).get_excel('community')[2]
    # data['param']['access_token']='88e613d776dc5db771b4bb418d96086d'
    param=eval(data['param'])
    param['access_token']='88e613d776dc5db771b4bb418d96086d'
    data['param']=param
    res=re1.http_request(data['url'],data['param'],data['HttpMethod'],headers=header,verify=False)
    print(res.json())
    # print(res.json()['data']['tid'])

    # httpr=requests.delete(data['url'],params=data['param'],headers=header,verify=False)
    # print(httpr.json())
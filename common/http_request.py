#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/814:22
#文件     :
#IDE      :PyCharm

import requests,json

OKGREEN = '\033[32m'
ERROR = '\033[31m'
WARNING = '\033[33m'
END = '\033[0m'
header={'User-Agent':'bz-mindfulness-android-1.5.1 from android sdk version:24 mobile versionCode:7.0 phone model:PRO 7-H BZChannelNo-baidu',
        'Content-Type':'application/x-www-form-urlencoded'}

class HttpRequtser:

    def http_request(self,url,param,http_method,**kwargs):

        if http_method.upper()=='POST':
            try:
                res=requests.post(url,param,**kwargs)
                print(OKGREEN+'正在进行post请求 ')
            except Exception as e:
                print("post请求出现了异常:{0}".format(e))
        elif http_method.upper()=='PUT':
            try:
                res=requests.put(url,param,**kwargs)
                print('正在进行PUT请求 ')
            except Exception as e:
                print("PUT请求出现了异常:{0}".format(e))
        elif http_method.upper()=='DELETE':
            try:
                res = requests.delete(url,param,**kwargs)
                print('正在进行DELETE请求 ')
            except Exception as e:
                print("DELETE请求出现了异常:{0}".format(e))
        else:
            try:
                res=requests.get(url,param,**kwargs)
                print(OKGREEN+'正在进行get请求 ')
            except Exception as e:
                print("get请求出现了异常:{0}".format(e))

        # access_token=res['data']['access_token']
        # print("http请求的结果是:{0}".format(access_token))
        return res

if __name__=='__main__':
    re1=HttpRequtser()
    import time
    url='https://account.office.bzdev.net/restful/register/getappmobilecaptcha.json'
    data={'captcha_type':'member_register','captcha_count':1,'phone_prefix':86,'mobile':13200000004}
    r=re1.http_request(url,data,'post',verify=False,headers=header)
    # r = requests.post(url, data, 'post', verify=False,headers=header)
    print(r.json())
    code=r.json()['data']['idstring']

    time.sleep(1)
    url = 'https://account.office.bzdev.net/restful/app/codelogin.json'
    data = {'is_debug': 0, 'mobilecaptcha':code, 'phone_prefix': 86, 'phone': 13200000004,'type':1}

    lo=re1.http_request(url,data,'post',verify=False,headers=header)
    print(lo.json())
    token=None
    if lo.json()['data']['access_token']:
        # header['access_token']=tokin
        token = lo.json()['data']['access_token']
        print(111)
    print(header)
    time.sleep(1)

    url = 'https://api.office.bzdev.net/mindfulness/restful/member/profile.json'
    data={'access_token':token}
    pro=re1.http_request(url,data,'get',headers=header,verify=False)
    print(pro.json())
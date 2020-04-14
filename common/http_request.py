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


class HttpRequtser:
    cookies = None
    def http_request(self,url,param,http_method,cookies):
        if http_method.upper()=='POST':
            try:
                res=requests.post(url,param,cookies=cookies)
                print(OKGREEN+'正在进行post请求 ')
            except Exception as e:
                print("post请求出现了异常:{0}".format(e))
        elif http_method.upper()=='PUT':
            try:
                res=requests.put(url,param,cookies=cookies)
                print('正在进行post请求 ')
            except Exception as e:
                print("post请求出现了异常:{0}".format(e))
        elif http_method.upper()=='DELETE':
            try:
                res = requests.delete(url,param,cookies=cookies)
                print('正在进行post请求 ')
            except Exception as e:
                print("post请求出现了异常:{0}".format(e))
        else:
            try:
                res=requests.get(url,param,cookies=cookies)
                print(OKGREEN+'正在进行post请求 ')
            except Exception as e:
                print("post请求出现了异常:{0}".format(e))

        # access_token=res['data']['access_token']
        # print("http请求的结果是:{0}".format(access_token))
        return res

if __name__=='__main__':
    res=HttpRequtser()

    r=res.http_request(url,data,'post',cookies=None)
    print(r.json())
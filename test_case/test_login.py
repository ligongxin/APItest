#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/1016:23
#文件     :
#IDE      :PyCharm

from common.http_request import HttpRequtser
from common.do_excel import DoExce
from common import project_path
import unittest
from ddt import ddt,data
from common.my_log import MyLog
from common.do_mysql import DoMysql

test_data=DoExce(project_path.test_case_path).get_excel('login')

header={'User-Agent':'bz-mindfulness-android-1.5.1 from android sdk version:24 mobile versionCode:7.0 phone model:PRO 7-H BZChannelNo-baidu',
        'Content-Type':'application/x-www-form-urlencoded'}
TOKEN=None
@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.logger=MyLog()
        self.logger.info('开始测试')
        print('开始测试')
    @data(*test_data)
    def test_login(self,data_item):
        global TOKEN
        print('正在进行第{0}条用例:{1}'.format(data_item['id'],data_item['description']))
        self.logger.info('正在进行第{0}条用例:{1}'.format(data_item['id'],data_item['description']))
        params=eval(data_item['param'])

        if data_item['module']=='登录':
            if params['mobilecaptcha']=='code':
                #去数据库查询验证码替换
                for i in [2]:

                    sql = 'SELECT idstring FROM `pre_captcha_mobile` WHERE mobile={0} ORDER BY captchaid DESC LIMIT 1'.format(params['phone'])
                    code = DoMysql().do_mysql(sql)
                params['mobilecaptcha']=code[0][0]
        else:
            params['access_token'] = TOKEN

        print('测试数据为{0}'.format(params))
        self.logger.info('测试数据为{0}'.format(params))

        res=HttpRequtser().http_request(data_item['url'],params,data_item['HttpMethod'],verify=False,headers=header)
        print('测试结果是{0}'.format(res.json()))
        self.logger.info('测试结果是{0}'.format(res.json()))
        if data_item['module'] == '登录':
            if res.json()['data']['access_token']:  # 任何非空数据的布尔值都为True  cookies是一个类字典的格式
                TOKEN = res.json()['data']['access_token']  # 如果cookies不为空 就替换全局变量的COOKIES 修改全局变量
        try:
            self.assertEqual(str(data_item['ExpectedResult']),str(res.json()['error_code']))
            self.assertEqual(res.status_code,200)
            print('用例通过')
            self.logger.info('用例通过')
            TestResult='PASS'
            Comment=None
        except AssertionError as e:
            print('用例失败错误是{}'.format(e))
            self.logger.error('用例失败错误是{}'.format(e))
            TestResult = 'Failed'
            Comment=res.json()['error_message']
            raise e
        finally:
            DoExce(project_path.test_case_path).write_back('login',data_item['id']+1,res.json()['error_code'],TestResult,Comment)


    def tearDown(self):
        print('用例结束')
        self.logger.info('用例结束')



#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/10/2114:19
#文件     :
#IDE      :PyCharm

from common.http_request import HttpRequtser
from common.do_excel import  DoExce
from common import project_path
import unittest
from ddt import ddt,data
from common.my_log import MyLog
from common.do_mysql import DoMysql
from common.get_info_data import GetInfoData,Application_profiles


test_data=Application_profiles(DoExce(project_path.test_case_path).get_excel('account'))

@ddt
class TestAccount(unittest.TestCase):
    def setUp(self):
        self.logger=MyLog()
        self.logger.info('开始测试')

    def tearDown(self):
        print('用例结束')
        self.logger.info('用例结束')
    @data(*test_data)
    def test_account(self,data_item):
        print('正在进行第{0}条用例:{1}'.format(data_item['id'], data_item['description']))
        self.logger.info('正在进行第{0}条用例:{1}'.format(data_item['id'], data_item['description']))
        params = eval(data_item['param'])
        params['access_token']=GetInfoData().get_token()

        print('测试数据为{0}'.format(params))
        self.logger.info('测试数据为{0}'.format(params))

        res = HttpRequtser().http_request(data_item['url'], params, data_item['HttpMethod'], verify=False,
                                          headers=GetInfoData().get_hander())
        print('测试结果是{0}'.format(res.json()))
        self.logger.info('测试结果是{0}'.format(res.json()))

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

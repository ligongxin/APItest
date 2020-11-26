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
from common.get_info_data import GetInfoData,Application_profiles
#替换ulr的环境域名
test_data=Application_profiles(DoExce(project_path.test_case_path).get_excel('mindfulness'))

@ddt
class TestApi(unittest.TestCase):
    '''文章，背景音的接口'''
    def setUp(self):
        self.logger=MyLog()
        self.logger.info('开始测试')
        print('开始测试')
    @data(*test_data)
    def test_api(self,data_item):
        # data_item=Application_profiles(data_item)
        print('正在进行第{0}条用例:{1}'.format(data_item['id'],data_item['description']))
        self.logger.info('正在进行第{0}条用例:{1}'.format(data_item['id'],data_item['description']))

        print('测试数据为{0}'.format(data_item['param']))
        self.logger.info('测试数据为{0}'.format(data_item['param']))

        res=HttpRequtser().http_request(data_item['url'],eval(data_item['param']),data_item['HttpMethod'],verify=False,headers=GetInfoData().get_hander())
        print('测试结果是{0}'.format(res.json()))
        self.logger.info('测试结果是{0}'.format(res.json()))
        # if res.cookies:  # 任何非空数据的布尔值都为True  cookies是一个类字典的格式
        #     COOKIES = res.cookies  # 如果cookies不为空 就替换全局变量的COOKIES 修改全局变量
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
            DoExce(project_path.test_case_path).write_back('mindfulness',data_item['id']+1,res.json()['error_code'],TestResult,Comment)


    def tearDown(self):
        print('用例结束')
        self.logger.info('用例结束')



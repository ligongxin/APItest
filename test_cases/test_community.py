#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/11/2711:07


from common.http_request import HttpRequtser
from common.do_excel import DoExce
from common import project_path
import unittest
from ddt import ddt,data
from common.my_log import MyLog
from common.do_mysql import DoMysql
from common import setting
from common.get_info_data import GetInfoData,Application_profiles

#替换ulr的环境域名
test_data=Application_profiles(DoExce(project_path.test_case_path).get_excel('community'))
RID=None
@ddt
class TestCommunity(unittest.TestCase):
    '''社区'''
    def setUp(self):
        self.logger=MyLog()
        self.logger.info('开始测试')

    @data(*test_data)
    def test_community(self, data_item):
        self.logger.info('正在进行第{0}条用例:{1}'.format(data_item['id'], data_item['description']))
        #查找tid，cid，rid并替换
        if data_item['param'].find('${tid}')!=-1:
            data_item['param']=data_item['param'].replace('${tid}', str(getattr(GetInfoData,'RID')))
        params = eval(data_item['param'])
        #添加token
        params['access_token'] = GetInfoData().get_token()

        self.logger.info('测试数据为{0}'.format(params))
        #发送请求
        res = HttpRequtser().http_request(data_item['url'],params , data_item['HttpMethod'],
                                          verify=False, headers=GetInfoData().get_hander())
        self.logger.info('测试结果是{0}'.format(res.json()))
        try:
            #断言
            self.assertEqual(str(data_item['ExpectedResult']),str(res.json()['error_code']))
            self.assertEqual(res.status_code,200)
            self.logger.info('用例通过')
            TestResult='PASS'
            Comment=None
            if data_item['description'] == '发布动态':
                tid = res.json()['data']['tid']
                # 替换info里的tid
                global RID
                setattr(GetInfoData,'RID',tid)
                # GetInfoData().get_community_id(0, 'tid', str(tid))
                print(getattr(GetInfoData,'RID'))
        except AssertionError as e:
            self.logger.error('用例失败错误是{}'.format(e))
            TestResult = 'Failed'
            Comment=res.json()['error_message']
            raise e
        finally:
            DoExce(project_path.test_case_path).write_back('community',data_item['id']+1,res.json()['error_code'],TestResult,Comment)

    def tearDown(self):
        self.logger.info('用例结束')


if __name__ == '__main__':
    unittest.main()
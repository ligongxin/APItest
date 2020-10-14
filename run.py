#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/1014:46
#文件     :
#IDE      :PyCharm
'''
from faker import Faker

fak=Faker(locale='zh_CN')

name=fak.name()
print(name)
print(fak.address())
print(fak.text())
print(fak.ssn())'''


import unittest

from common.send_email import sendEmail

from common import project_path
from common import HTMLTestRunnerNew
from test_cases.test_api import TestApi
from test_cases.test_login import TestLogin

suite=unittest.TestSuite()
loader=unittest.TestLoader()

#加载测试用例
suite.addTest(loader.loadTestsFromTestCase(TestApi))
suite.addTest(loader.loadTestsFromTestCase(TestLogin))

#执行测试用例
# runner=unittest.TextTestRunner()
# runner.run(suite)
with open(project_path.report_path,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='接口测试',description='11111',tester='lgx')
    runner.run(suite)





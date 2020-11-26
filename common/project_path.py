#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/1014:47
#文件     :
#IDE      :PyCharm

import os

p_path=os.path.realpath(__file__)
Project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
p=os.path.split(os.getcwd())[0]

#测试用例路径
test_case_path=os.path.join(Project_path,'test_data','mindfulness.xlsx')

#数据库配置路径
db_config_path=os.path.join(Project_path,'config','db_config')

#日志报告路径的配置
log_path=os.path.join(Project_path,'test_result','logs','test_api.txt')

#日志
logs_path=os.path.join(Project_path,'report','log','testApi_log.txt')

#html报告
report_path=os.path.join(Project_path,'report','html_report','report.html')

#beafult_html
beafultHtml_path=os.path.join(Project_path,'report','html_report')


#用例路径
case_path=os.path.join(Project_path,'test_cases')
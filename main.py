#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/10/2318:39
#文件     :
#IDE      :PyCharm



import pytest
import subprocess
if __name__ == '__main__':
    # pytest.main()  # 执行pytest命令，去收集用例，然后执行用例。当前文件所在的目录为rootdir
    pytest.main(["--alluredir=report/allure_testresult_files"])  #生成allure报告
    subprocess.check_output('allure serve report/allure_testresult_files', shell=True)
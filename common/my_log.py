#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/2817:10
#文件     :
#IDE      :PyCharm

import logging
from common import project_path

class MyLog:
    def my_log(self,level,msg):
        my_logger=logging.getLogger("mindfulness")
        my_logger.setLevel("DEBUG")#设置

        #创造一个专属输出渠道  过滤 和排版
        #格式：
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        ch=logging.StreamHandler()#输出到控制台
        ch.setLevel("DEBUG")#设置输出级别  大写
        ch.setFormatter(formatter)

        fh=logging.FileHandler(project_path.logs_path,encoding='UTF-8')#输出到制定文件
        fh.setLevel("DEBUG")#设置输出级别  大写
        fh.setFormatter(formatter)

        #对接起来 给日志收集器添加一个渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)

        # #渠道要记得移除掉 否则 日志输出会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log("DEBGU",msg)

    def info(self,msg):
        self.my_log("INFO",msg)

    def warning(self,msg):
        self.my_log("ERROR",msg)

    def error(self,msg):
        self.my_log("WARNING",msg)

    def critical(self,msg):
        self.my_log("CRITICAL",msg)




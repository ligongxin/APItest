#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/1014:46
#文件     :
#IDE      :PyCharm

from faker import Faker

fak=Faker(locale='zh_CN')

name=fak.name()
print(name)
print(fak.address())
print(fak.text())
print(fak.ssn())
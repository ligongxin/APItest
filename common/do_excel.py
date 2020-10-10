#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/1014:49
#文件     :
#IDE      :PyCharm
from openpyxl import load_workbook
from common import project_path

class DoExce():
    def __init__(self,file_name):
        self.file_name=file_name

    #读取Excel的数据
    def get_excel(self,sheetname):
        wb = load_workbook(self.file_name)
        sheet=wb[sheetname]
        test_data=[]
        for i in range(2,sheet.max_row+1):
            sub_data={}
            sub_data['id'] = sheet.cell(i, 1).value  # 用例序号
            sub_data['HttpMethod'] = sheet.cell(i, 2).value
            sub_data['module'] = sheet.cell(i, 3).value
            sub_data['description'] = sheet.cell(i, 4).value
            sub_data['url'] = sheet.cell(i, 5).value
            sub_data['param']=sheet.cell(i,6).value
            sub_data['ExpectedResult']=sheet.cell(i,7).value
            test_data.append(sub_data)
        return test_data

    def write_back(self,sheet_name,row,ActualResult,TestResult):
        wb=load_workbook(self.file_name)
        sheet=wb[sheet_name]
        sheet.cell(row,8).value=ActualResult
        sheet.cell(row, 9).value = TestResult

        #保存
        wb.save(self.file_name)

if __name__=='__main__':

    sheet_name='mindfulness'
    wb=DoExce(project_path.test_case_path).get_excel(sheet_name)
    print(wb)
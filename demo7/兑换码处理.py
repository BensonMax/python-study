#coding=utf-8
import time
import json
import pandas
from openpyxl import Workbook

input_file_name = input("请您输入要复制的文件名:")
wb = Workbook()
dest_filename = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'生成的兑换码列表.xlsx'
ws1 = wb.active
ws1.title = "兑换码列表"
data = [];

with open(input_file_name, 'r') as f:
    data = data + json.load(f)

i = 0;

for (item) in data:
    i = i+1
    col_A = 'A%s' % (i)
    col_B = 'B%s' % (i)
    col_C = 'C%s' % (i)
    col_D = 'D%s' % (i)

    ws1[col_A] = item['redeem_code']
    ws1[col_B] = item['start_time']
    ws1[col_C] = item['end_time']
    ws1[col_D] = item['reward_info']

wb.save(filename = dest_filename)
position = dest_filename.rfind('.')
data_xls = pandas.read_excel(dest_filename, index_col=0)
data_xls.to_csv(dest_filename[0:position]+'.csv', encoding='utf-8')
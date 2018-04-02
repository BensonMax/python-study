#coding=utf-8

import pandas

def xlsx_to_csv_pd():
    input_file_name = input("请您输入处理的文件名:")
    position = input_file_name.rfind('.')
    data_xls = pandas.read_excel(input_file_name, index_col=0)
    data_xls.to_csv(input_file_name[0:position]+input_file_name[position:], encoding='utf-8')

if __name__ == '__main__':
    xlsx_to_csv_pd()
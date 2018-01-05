#  -*- coding:utf-8 -*-
# import csv
import sys
import xlrd
import re
sys.path.append('../..')
from data import *

'''csv文件读取'''
# with open('../../data/name_password.csv',  'r') as file:
#     data = csv.reader(file)
#     for name in data:
#         print(name[0] )

'''
	读取excel文件；	
	将一个excel中的具体的一个sheet转化成一个list返回，
	list中的每一个元素都是一个dict
'''
def open_excel(file = '../../data/name.xls'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except NameError:
		print("File not exits!")

def excel_table_byname(file='../../data/name.xls', colnameindex=0, by_name=u'Sheet1'):
	data = open_excel(file)
	table = data.sheet_by_name(by_name)
	nrows = table.nrows
	colnames = table.row_values(colnameindex)
	list_names = []
	for rownum in range(1, nrows):
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i]
			list_names.append(app)
	return list_names


#-----------------------数组中的每个元素都是一个字典
# def login_data():
# 	tables = excel_table_byname()
# 	dict1 = tables[0]
# 	print(dict1["name"])
# 	print(dict1["password"])

# if __name__ == '__main__':
# 	login_data()

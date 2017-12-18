#  -*- coding:utf-8 -*-
import csv
import sys
import xlrd
import re
sys.path.append('../..')
from data import *

# with open('../../data/name_password.csv',  'r') as file:
#     data = csv.reader(file)
#     for name in data:
#         print(name[0] )
data  = xlrd.open_workbook('../../data/name.xls')

sheet1 = data.sheet_by_name(u'Sheet1')
name1 = sheet1.cell(0, 0).value
password1 = sheet1.cell(0, 1).value
print(name1)
print(password1)
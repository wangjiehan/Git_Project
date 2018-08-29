'''
从test.xlsx读取、修改，生成一个新的、最终final.xls
'''
import os
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.basename(os.path.realpath(__file__)))

def file_path(file_dir):
	for root, files in os.walk(file_dir):
		return root, files
a = file_path(os.path.dirname(os.path.realpath(__file__)))
print(a[0])
print(a[1])

import xlrd
from xlutils.copy import copy
rb = xlrd.open_workbook('test.xlsx')
wb = copy(rb)
ws = wb.get_sheet(0)
ws.write(0,7,'本地路径')
for i in range(len(a[1]) - 3):		# 三个非视频文件
	ws.write(1 + i, 7, str(a[0] + '\\' + a[1][i]))
wb.save('final.xls')

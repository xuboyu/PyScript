# -*- coding:utf-8 -*-

# 遍历获取需求文件
# Cory_boyu

import sys, getopt
import os
import xlrd
import re

# def main(argv):

# #获取命令行的文件参数
# try:
#     opts, args = getopt.getopt(argv, "hi:", ["ifile="])
# except getopt.GetoptError:
#     print('getCollect.py -i <inputfile>')
#     sys.exit(2)
# for opt, arg in opts:
#     if opt == '-h':
#         print('getCollect.py -i <inputfile>')
#         sys.exit()
#     elif opt in ("-i", "--ifile"):
#         inputfile = arg
#         print ('输入的文件为：', inputfile)

file = 'C:\\Users\\Administrator\\Desktop\\联运删测包名＆参数.xlsx'
# file = inputfile

# 打开excel
xls = xlrd.open_workbook(file)

# 操作excel
xls.sheet_names() # 获取excel里的工作表sheet名称数组
sheet = xls.sheet_by_name('Sheet1')

# 获取整列的值，返回一个列表
qudaos = sheet.col_values(2)#渠道
baomings = sheet.col_values(4)#包名

#删除无用数据
qudaos.pop(1)
qudaos.pop(2)
baomings.pop(1)
baomings.pop(2)

# 数组转换操作
#渠道名操作
xqudao = []
xbaoming = []
hebing = []
for qudao in qudaos:
    xqudao.append(qudao)
#包名操作
for baoming in baomings:
    xbaoming.append(baoming)

xbaoming.remove("")
xqudao.remove("")

#数据合并
# {{"渠道名","包名"},{"渠道名","包名"}...}
str = ""
last = []
for i,a in enumerate(xqudao):
    str = a,xbaoming.__getitem__(i)
    last.append(str)
s = last.__str__()
print(s)

file = open('E:/packtool/pcb/collect.txt','w')
file.write(last.__str__())

# if __name__ == "__main__":
#    main(sys.argv[1:])
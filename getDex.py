#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import zipfile
import random
import string

apk = "F:/download/yx4c.ssjtj.android.game_b8350b4b61.apk" # this is apk files' store path
dex_path = "E:/packtool/dex2jar/" # a directory  store dex files

portion = os.path.splitext(apk)
apkname = portion[0]

# def apk2dext(filepath):
'''
    将apk中的dex文件提取出来
    :param filepath: apk文件路径
    :return: 命中：True
'''
# 直接用zipfule.ZipFile处理.apk文件
apkfile = zipfile.ZipFile(apk, 'r')

if os.path.isdir('dex') == False:
    os.mkdir('dex')
# 将apk内所有.dex文件都生成在'dex/'路径下
for tempfile in apkfile.namelist():  # 遍历apk包内的所有文件名
    if tempfile.endswith('.dex'):
        dexfilename = apkname + ".dex"
        f = open(dex_path, 'w+')
        f.write(apkfile.read(tempfile))

# return True
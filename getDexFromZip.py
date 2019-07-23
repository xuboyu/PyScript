#!/usr/bin/env python
# coding=utf-8

import os
import zipfile
import shutil

apk = "F:/download/yx4c.ssjtj.android.game_b8350b4b61.apk" # this is apk files' store path
dex_path = "E:/packtool/dex2jar" # a directory  store dex files

# apklist = os.listdir(path) # get all the names of apps

# if not os.path.exists(dex_path):
#     os.makedirs(dex_path)

portion = os.path.splitext(apk)

newname = portion[0] + ".zip" # 修改apk为zip的包体命名
old = portion[0] + ".apk" # 获取dex后恢复命名为apk
print("new:"+newname)
print("old:"+old)

#改名
os.rename(apk,newname)

apkname = portion[0]

#zip_apk_path = os.path.join(path,APK) # get the zip files
zip_apk_path = newname

z = zipfile.ZipFile(zip_apk_path, 'r') # read zip files

#print filename
for filename in z.namelist():
    #print filename
    if filename.endswith(".dex"):
        print("--- 检查到dex文件：" + filename)
        dexfilename = apkname + ".dex"
        print("--- 开始重命名：" + dexfilename)
        dexfilepath = os.path.join(dex_path, dexfilename)
        f = open(dexfilepath, 'wb+') # eq: cp classes.dex dexfilepath
        f.write(z.read(filename))
        f.close()
        print("--- 开始移动提取dex文件")
        shutil.move(dexfilename,dex_path)
        print("--- 移动成功，dex已移动至："+dex_path)





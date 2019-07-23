import os

apk = "F:/download/yx4c.ssjtj.android.game_b8350b4b61.zip" # this is apk files' store path
dex_path = "E:/packtool/dex2jar" # a directory  store dex files

# for APK in apklist:
portion = os.path.splitext(apk)

newname = portion[0] + ".apk" # 修改apk为zip的包体命名

if apk.endswith(".zip"):
    os.rename(apk,newname)
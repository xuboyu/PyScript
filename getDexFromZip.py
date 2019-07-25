import os, zipfile, shutil, getopt, sys

def main(argv):

    #获取命令行参数
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ifile=","outFile="])
    except getopt.GetoptError:
        print("getDexFromZip.py -i <dexFile> -o <outputFile>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-i":
            dexFile = arg
            print("dex所在文件位置：",dexFile)
        elif opt == "-o":
            outputFile = arg
            print("dex输出路径为：",outputFile)
        elif opt == "-h":
            print("getDexFromZip.py -i <dexFile> -o <outputFile>")

    portion = os.path.splitext(dexFile)

    newname = portion[0] + ".zip" # 修改apk为zip的包体命名
    old = portion[0] + ".apk" # 获取dex后恢复命名为apk
    print("---new:"+newname)
    print("---old:"+old)

    #改名
    os.rename(dexFile,newname)
    apkname = portion[0]

    zip_apk_path = newname
    z = zipfile.ZipFile(zip_apk_path, 'r') # read zip files

    for filename in z.namelist():
        #print filename
        if filename.endswith(".dex"):
            print("--- 检查到dex文件：" + filename)
            dexfilename = apkname + ".dex"
            print("--- 开始重命名：" + dexfilename)
            dexfilepath = os.path.join(outputFile, dexfilename)
            f = open(dexfilepath, 'wb+') # eq: cp classes.dex dexfilepath
            f.write(z.read(filename))
            f.close()
            print("--- 开始移动提取dex文件")
            shutil.move(dexfilename,outputFile)
            print("--- 移动成功，dex已移动至："+outputFile)

if __name__ == "__main__":
    main(sys.argv[1:])





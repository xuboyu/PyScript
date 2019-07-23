'''
删除指定文件
python deleteFile.py -i <deleteFile>
<deleteFile>为删除文件路径
'''

import os, shutil, getopt, sys

def main(argv):

    #获取命令行参数
    try:
        opts, args = getopt.getopt(argv, "hi:",["ifile="])
    except getopt.GetoptError:
        print('deleteFile.py -i <deleteFile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt != "-i":
            print('deleteFile.py -i <deleteFile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            deleteFile = arg
            print("指定删除文件为：", deleteFile)
            apk = deleteFile

    os.remove(apk) #执行删除
    print("--- 文件删除成功："+apk)

if __name__ == "__main__":
    main(sys.argv[1:])
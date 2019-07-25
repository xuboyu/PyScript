import os, getopt, sys

def main(argv):

    #获取命令行参数
    try:
        opts, args = getopt.getopt(argv, "hi:n:",["ifile=","newName="])
    except getopt.GetoptError:
        print("changeFileName.py -i <fileName> -n <newName>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-i":
            fileName = arg
            print("---需要修改的文件为：", fileName)
        elif opt == "-n":
            newName = arg
            print("---需要修改为：", newName)
        elif opt != "-i" or opt != "-n":
            print("changeFileName.py -i <fileName> -n <newName>")

    portion = os.path.splitext(fileName)

    os.rename(fileName,newName)
    print("---执行成功，文件名已修改")

if __name__ == "__main__":
    main(sys.argv[1:])
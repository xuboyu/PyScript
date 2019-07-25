import sys, getopt, os, xlrd, re

def main(argv):

    #获取命令行的文件参数
    try:
        opts, args = getopt.getopt(argv, "hi:o:s:r:c:", ["ifile=","outPutFile=","sheet=","row=","column="])
    except getopt.GetoptError:
        print("getCollect.py -i <inputfile> -o <outPutFile> -s <sheet> -r <row> -c <column>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("getCollect.py -i <inputfile> -o <outPutFile> -s <sheet> -r <row> -c <column>")
            sys.exit()
        elif opt == "-i":
            collectFile = arg
            print ("---需要遍历的文件为：", collectFile)
        elif opt == "-o":
            outputFile = arg
            print("---输出路径为：",outputFile)
        elif opt == "-s":
            sheet = arg
            print("---要遍历的表：",sheet)
        elif opt == "-r":
            row = arg
            print("---操作行为：",row)
        elif opt == "-c":
            column = arg
            print("---操作列为：",column)

    # 打开excel
    xls = xlrd.open_workbook(collectFile)

    # 操作excel
    xls.sheet_names() # 获取excel里的工作表sheet名称数组
    sheet = xls.sheet_by_name(sheet)

    # 获取整列的值，返回一个列表
    qudaos = sheet.col_values(2)#渠道
    baomings = sheet.col_values(4)#包名

    #删除无用数据，特殊处理
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

    file = open(outputFile,'w')
    file.write(last.__str__())

if __name__ == "__main__":
   main(sys.argv[1:])
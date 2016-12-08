#-*- coding:utf-8 -*-
####python2.7
import os

#执行函数
def getDirInfo(path):
    #建立两个变量分别记录文件大小信息和文件数量
    result = []
    items = 0
    #遍历传入的路径
    for root,dirs,files in os.walk(path):
        #for循环分别得到文件大小并添加到result中
        for file in files:
            size = os.path.getsize(root+os.sep+file)
            #构造list添加到result
            #os.sep为系统分割符，windows下相当于'\\'
            result.append([root+os.sep+file,size])
            #文件计数
            items += 1
    #对结果排序
    result = sorted(result,key=lambda i:i[0])
    #打印结果
    for i in result:
        print '文件 ',i[0].decode('gbk'),' 占用',i[1],' 字节'
    print '文件夹 ', path.decode('gbk'),' 下共有',items,'个文件'

#主函数
def main():
    print '输入文件路径'
    path = raw_input('>>>')
    if os.path.exists(path):
        getDirInfo(path)
    else:
        print '路径有误'
#启动
if __name__ == '__main__':
    main()
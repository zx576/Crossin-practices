#-*- coding:utf-8 -*-
import shutil
import os
import re

#遍历文件并组装图片和视频地址
def getFile(path):
    #建立三个list分别存放所有文件地址、图片地址、视频地址
    pictures = []
    videos = []
    all_files = []
    #遍历指定文件夹所有文件
    for root,dirs,files in os.walk(path):
        for file in files:
            #放入文件地址
            all_files.append(root + os.sep + file)

    #对所有文件地址进行筛选
    pic_compile = re.compile(r'.+\.jpg|.+\.png|.+\.jpeg|.+\.gif', re.I)
    video_compile = re.compile(r'.+\.avi|.+\.rmvb|.+\.rm|.+\.mkv', re.I)
    #匹配all_files中的对象
    for file in all_files:
        picture_file = re.search(pic_compile,file)
        if picture_file:
            pictures.append(picture_file.group())
        video_file = re.search(video_compile,file)
        if video_file:
            videos.append(video_file.group())
    return pictures,videos

#移动文件传入参数分别为图片地址列表、视频地址列表、存放图片文件夹、存放视频文件夹
def moveFile(pictures,videos,pic_root,video_root):
    for pic_add in pictures:
        shutil.move(pic_add,pic_root)
    for video_add in videos:
        shutil.move(video_add,video_root)

#主函数
def main():
    print '输入您要整理的地址'
    path = ''
    #输入判断
    while True:
        path = raw_input('>>>>>')
        if os.path.exists(path):
            break
        else:
            print '地址无效'
    #分别得到图片视频地址
    files = getFile(path)
    pic_adds = files[0]
    video_adds = files[1]
    #在输入的path下新建文件夹
    try:
        os.mkdir(path+os.sep+'newpic')
        os.mkdir(path + os.sep + 'newvideo')
    except:
        print '存放文件夹已建立'
    finally:
        pic_path = path+os.sep+'newpic'
        video_path = path+os.sep+'newvideo'
    #移动文件
    moveFile(pic_adds,video_adds,pic_path,video_path)
    print 'success'

if __name__ == '__main__':
    main()
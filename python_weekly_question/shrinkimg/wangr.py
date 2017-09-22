import os
import argparse
from PIL import Image
import imghdr


def im_co(infile, ratio, out, delete_ori):  #压缩图片
    """
    infile     输入文件的名称，如果是一个文件夹，则压缩文件夹内的所有图片
    ratio      压缩的比率
    out        输出文件的路径，文件名为原名加前缀；如果没有指定，则保存在原文件夹
    delete_ori 选择是否删除原文件
    """

    out_pre = 'out_'  

    if os.path.isdir(infile):
        file_list = os.listdir(infile)  #得到文件夹内所有文件的名称列表
        for i in range(len(file_list)):
            file_list[i] = os.path.join(infile, file_list[i])
    else:
        file_list = [infile]
    if out:
        if not os.path.exists(out): #如果指定的文件夹不存在，则创建
            os.mkdir(out)
        out_file_pre = os.path.join(out, out_pre)
    else:
        if os.path.isdir(infile):
            out_file_pre = os.path.join(infile, out_pre)
        else:
            out_file_pre = os.path.join(os.path.dirname(infile), out_pre)
    for i in file_list:
        try:
            if imghdr.what(i):  #如果是图片文件
                im = Image.open(i)
                width, height = im.size
                out_filename = out_file_pre + os.path.basename(i)
                new_width, new_height = int(width*ratio), int(height*ratio) #压缩后尺寸
                im = im.resize((new_width, new_height))
                if delete_ori:
                    os.remove(i)
                im.save(out_filename)
        except:
            continue
        
if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog="压缩图片")
    parse.add_argument('infile', help='输入文件的名称，\
                    如果是一个文件夹，则 %(prog)s 压缩文件夹内的所有图片')
    parse.add_argument('ratio', type=float, help='压缩的比率')
    parse.add_argument('-o', dest='out_path', help='输出文件的路径，\
                    文件名为原名加前缀 `out_`，默认在原文件夹')
    parse.add_argument('-d', dest='delete_ori', action='store_true', 
                    help='选择是否保留原文件，默认保留')
    args = parse.parse_args()

    im_co(args.infile, args.ratio, args.out_path, args.delete_ori)
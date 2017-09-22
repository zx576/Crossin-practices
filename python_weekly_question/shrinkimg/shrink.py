#coding=utf-8

import argparse
import os

from PIL import Image

def parse():

	parser = argparse.ArgumentParser(description='process images')

	help_pic_addr = '某张图片地址或某个文件夹地址，支持相对地址和绝对地址'
	parser.add_argument('--addr', type=str, help=help_pic_addr, default=None)

	help_ratio = '图片缩小比例，接受一个 float 型参数，默认为 1.0'
	parser.add_argument('--ratio', type=float, help=help_ratio, default=1.0)

	help_save_directory = '文件保持地址, 支持相对地址和绝对地址'
	parser.add_argument('--dest', type=str, help=help_save_directory, default='.')

	help_if_delete = '是否删除源文件，默认为 False'
	parser.add_argument('--delete', type=bool, help=help_if_delete, default=False)


	args = parser.parse_args()
	return args

def is_img(addr):

	# 尝试打开该地址
	# 不能被打开可能是路径错误或者文件类型错误
	try:
		im = Image.open(addr)
		return True

	except Exception as e:
		print('处理 {} 文件时发生错误, 已经跳过该文件'.format(addr))
		return False

def get_pics_from_dir(path):

	# 遍历指定文件夹
	# 将所有图片地址添加到 res
	res = []
	for root, dirs, files in os.walk(path):
		for f in files:
			addr = os.path.join(root, f)
			if is_img(addr):
				res.append(addr)

	return res

def process(addrs, dest, ratio, delete):

	for file in addrs:
		# 缩小图片并保存
		im = Image.open(file)
		adjusted_size = tuple([int(i*ratio) for i in im.size])
		new = im.resize(adjusted_size)
		name = file.split('/')[-1]
		file_path = os.path.join(dest, name)
		# 查看目的文件夹是否已经存在该文件名
		# 存在则在文件名前添加 _ 
		while os.path.exists(file_path):
			name = '_' + name
			file_path = os.path.join(dest, name)
		new.save(file_path)
		print('文件 {0} 经处理后保存为 {1}'.format(file, name))

	# 是否删除
	if delete:
		for file in addrs:
			os.remove(file)
		print('原文件已经删除')

	
def dispatch(args):

	# 判断程序能否进行
	assert args.addr and os.path.exists(args.addr), '目标图片地址或者文件夹地址缺失或不存在'
	assert os.path.isdir(args.dest), '未找到文件存放目录'			


	pic_addrs = []
	# 检查是否含为文件夹
	if os.path.isdir(args.addr):
		pic_addrs = get_pics_from_dir(args.addr)
	# 检查是否为文件
	elif os.path.isfile(args.addr) and is_img(args.addr):
		pic_addrs.append(args.addr)

	assert pic_addrs, '未找到有效的图片地址'

	delete = args.delete
	ratio = args.ratio
	dest = args.dest

	# 处理图片函数
	return process(pic_addrs, dest, ratio, delete)
		

if __name__ == '__main__':
	
	args = parse()
	dispatch(args)


'''

核心的代码如下


def process(addrs, dest, ratio, delete):

	# addrs 为所有待处理的图片地址 类型为　list
	#　dest 为某个文件夹路径 类型为 str
	# ratio 为缩小比例，　类型为 float
	# delete 为是否删除原文件标记，　类型为 bool
	for file in addrs:
		# 缩小图片并保存
		im = Image.open(file)
		adjusted_size = tuple([int(i*ratio) for i in im.size])
		new = im.resize(adjusted_size)
		name = file.split('/')[-1]
		file_path = os.path.join(dest, name)
		# 查看目的文件夹是否已经存在该文件
		# 存在则在文件名前添加 _ 
		while os.path.exists(file_path):
			name = '_' + name
			file_path = os.path.join(dest, name)
		new.save(file_path)
		print('文件 {0} 经处理后保存为 {1}'.format(file, name))

	# 是否删除
	if delete:
		for file in addrs:
			os.remove(file)
		print('原文件已经删除')


代码地址: https://gitee.com/zx576/Crossin-practices/blob/master/python_weekly_question/shrinkimg/shrink.py


完成该题目的同学有四位，
王任　同学的代码逻辑较完整，不仅考虑了正常的情况，也考虑了异常处理：https://paste.ubuntu.com/25589912/
其他完成题目的同学还有：
热风 同学：https://github.com/SumOfMinterm/PythonProjects-ImageProcessing/blob/master/resizeByArgs.py
古美萌 同学： https://coding.net/u/komikado/p/crossinweek/git/blob/master/img.py
Seerz 同学：https://paste.ubuntu.com/25513336/


'''

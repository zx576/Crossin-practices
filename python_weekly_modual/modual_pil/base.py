from PIL import Image


def t1():
    '''打开并显示文件'''
    im = Image.open('crawling.jpg')
    im.show()

# print(im.format,im.size,im.mode)

def t2():
    '''转换文件格式'''
    im = Image.open('crawling.jpg')
    im.save('c2.png')
    im = Image.open('c2.png')
    im.show()


def t3():
    '''生成缩略图'''
    size = (128,128)
    im = Image.open('crawling.jpg')
    im.thumbnail(size)
    im.save('c3.jpeg')

# t3()

def t4():
    '''生成子矩形'''
    box = (100,100,400,400)
    im = Image.open('crawling.jpg')
    region = im.corp(box)
    region = region.transpose(Image.ROTATE_180)
    im.paste(region,box)

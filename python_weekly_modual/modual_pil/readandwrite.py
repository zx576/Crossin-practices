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


# 示例代码
def r_and_w():
    '''图片文件的打开、格式转换、生成缩略图'''

    im = Image.open('raw2l.png')
    print(im.format,im.size,im.mode)

    # tol = im.convert('L')
    # tol.show()
    # tol.save('dw2L.png')
    #
    # im.save('c2.jpeg')
    #
    size = (128,128)
    im.thumbnail(size)
    im.save('dwthumb.jpeg')
    im.show()



r_and_w()

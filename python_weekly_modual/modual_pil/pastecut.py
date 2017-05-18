from PIL import Image


def t4():
    '''生成子矩形'''
    box = (100,100,400,400)
    im = Image.open('crawling.jpg')
    region = im.corp(box)
    region = region.transpose(Image.ROTATE_180)
    im.paste(region,box)



def paste():
    im1 = Image.open('dw.png')
    im2 = Image.open('dw2L.png')

    # print(im2.size)

    box = (0,0,400,600)
    region = im2.crop(box)
    region.show()
    # region = region.transpose(Image.ROTATE_180)
    # box = (150,150,450,450)
    # region.load()
    # im2.load()
    im1.paste(region,box)
    im1.show()
    im1.save('dw_mix.png')



paste()

def split_merge():
    im = Image.open('crawling.jpg')
    r, g, b = im.split()
    im = Image.merge('RGB',(r, b, g))
    im.show()


# split_merge()

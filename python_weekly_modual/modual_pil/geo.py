from PIL import Image


def resizxe_rotate():
    im = Image.open('mm.jpg')
    # im.show()
    # out = im.resize((100,100))
    # out.show()


    out = im.rotate(180)
    out.show()
    out.save('mm2.jpg')

resizxe_rotate()

def transpose_pic():
    im = Image.open('c2.png')
    # im.show()
    out = im.transpose(Image.ROTATE_90)

    out2 = im.transpose(Image.ROTATE_180)

    out.show()
    out2.show()


# transpose_pic()

from PIL import Image , ImageFont, ImageDraw

def drawtext():
    im = Image.open('addfont.png')
    print(im.size)
    font = ImageFont.truetype(r'BeaverScratches.ttf',70)
    print(font.getsize('xxxxx'))
    draw = ImageDraw.Draw(im)
    draw.text((100, 470), "tan90",font=font,fill=255)
    im.show()
    im.save('addfont2.png')


drawtext()

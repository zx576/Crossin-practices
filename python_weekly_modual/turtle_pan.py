from turtle import *
import time

def drawcorcle(radius,parts,color1,color2):
    pensize(1)
    speed(10)
    for i in range(parts):
        if i % 2 == 0:
            color(color1,color1)
        else:
            color(color2,color2)

        begin_fill()
        setheading(i*360/parts)
        forward(radius)
        left(90)
        circle(radius,360/parts)
        left(90)
        end_fill()

        penup()

        home()
        pendown()

drawcorcle(160,18,'yellow','red')
drawcorcle(150,18,'red','yellow')




time.sleep(10)

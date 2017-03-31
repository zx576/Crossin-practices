from turtle import *
import time

def house():

    speed(20)
    # fillcolor('brown')
    for i in range(10):
        home()
        pendown()

        goto(-i*4,-i*4)
        # color(214, 233, 248), color(214, 233, 248)
        setheading(60)
        color('green','green')
        begin_fill()
        forward(100)
        right(120)
        forward(100)
        setheading(-90)
        forward(100)
        right(90)
        forward(100)
        right(90)
        forward(100)
        end_fill()

        penup()

        home()
        goto(-i*4, -i * 4)
        pendown()
        setheading(60)
        color('brown','brown')
        begin_fill()
        forward(100)
        right(120)
        forward(100)
        left(90)
        forward(10)
        left(90)
        forward(117.32)
        left(120)
        forward(117.32)
        left(90)
        forward(10)
        end_fill()
        penup()



def drawcorcle(radius,parts,color1,color2):

    pendown()
    pensize(1)
    speed(20)

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

        goto(-200, 200)
        pendown()

    penup()



house()

goto(-200, 200)
drawcorcle(80,18,'yellow','red')

# goto(-100,170)
drawcorcle(50,18,'red','yellow')





time.sleep(5)


# coding=utf-8
import turtle
import time
import math


def shield():

    # 设置背景
    turtle.bgcolor('#010101')
    # 设置速度
    turtle.speed(10)

    # 依次填充同心圆
    fill_circle('#FF0000', 230, 178)
    fill_circle('#FFFFFF', 178, 129)
    fill_circle('#FF0000', 129, 75)
    fill_circle('#0000FF', 75)

    # 完成五角星
    draw_five('#FFFFFF', 75)

    turtle.done()


# 画圆线
def draw_circle(radium):

    turtle.home()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(radium)
    turtle.pendown()
    turtle.setheading(90)
    turtle.circle(radium)
    turtle.penup()
    turtle.home()


# 填充圆环
def fill_circle(color, r1, r2=0):
    turtle.color(color, color)
    turtle.fillcolor()
    turtle.begin_fill()
    draw_circle(r1)
    draw_circle(r2)
    turtle.end_fill()


# 画并填充五角星
def draw_five(color, radium):

    turtle.home()
    turtle.penup()
    turtle.setheading(90)

    turtle.forward(radium)
    turtle.setheading(288)
    turtle.pendown()

    long_side = (math.sin(math.radians(36))*radium)/math.sin(math.radians(126))

    turtle.color(color, color)
    turtle.fillcolor()
    turtle.begin_fill()

    for i in range(10):

        turtle.forward(long_side)
        if i % 2 == 0:
            turtle.left(72)
        else:
            turtle.right(144)
    turtle.end_fill()
    turtle.penup()


if __name__ == '__main__':
    shield()

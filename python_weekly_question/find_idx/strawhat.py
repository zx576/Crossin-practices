#!/usr/bin/env python
# *-*coding:utf-8 *-*

"""用 Python turtle模块画美国队长的盾牌"""

import turtle

turtle.bgcolor('black')
turtle.speed(10)
turtle.pensize(5)
turtle.pencolor('blue')


def fillcolor(colour):
    turtle.fillcolor(colour)
    turtle.begin_fill()


def circle(n=250):
    colors = ['red', 'white', 'red', 'blue', 'white']
    for i in range(4):
        turtle.pencolor(colors[i])
        # turtle.pencolor('black')
        fillcolor(colors[i])
        turtle.circle(n, 360)

        turtle.penup()
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        n -= 50
        turtle.pendown()
        turtle.end_fill()


def star():
    turtle.speed(1)
    turtle.pencolor('white')
    fillcolor('white')
    for i in range(5):
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.right(70)

    turtle.end_fill()


def draw():
    circle()

    turtle.right(90)
    turtle.penup()
    turtle.backward(10)

    turtle.right(90)
    turtle.backward(5)
    turtle.left(90)

    turtle.left(60)

    turtle.pendown()
    star()
    # input("Quit ")


draw()
turtle.done()
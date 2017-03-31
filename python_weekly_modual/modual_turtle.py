import turtle
import time

#
# color('red','white')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
#
# end_fill()
# done()

# 绘制四边形
# turtle.st()
# turtle.color('purple')
# turtle.pensize(5)
# turtle.speed(1)
#
# turtle.goto(0,0)
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#
# turtle.up()
# turtle.goto(-150,-200)
#
# turtle.color('red')
# turtle.write('Done')
# time.sleep(3)
# turtle.color('black','red')
# turtle.begin_fill()
# turtle.bgpic('1434.png')
# turtle.circle(80,180)
# turtle.delay(50)
# turtle.circle(60,180)
# turtle.end_fill()

# turtle.home()
# turtle.dot(20,'blue')
# turtle.forward(100)
# turtle.dot(40,'black')

# turtle.shape('circle')

# turtle.shapesize(5,2)
# turtle.tilt(30)
# turtle.textinput('name','>>>')
# turtle.numinput('POKER','your stake:',1000,20,10000)

# 控制画笔的速度
# turtle.speed(5)
# # 将画笔定位到原点
# turtle.goto(0,0)
# # 从原点开始，画出一个边长为100的正方形
# for i in range(4):
#     # 正向运动 100 的距离
#     turtle.forward(100)
#     # 向右偏 90 度
#     turtle.right(90)
#
# # 将画笔定位到原点
# turtle.home()
# # 画出一个半径为100，占3/4的圆
# turtle.circle(50,270)
#
# # 控制画笔的速度
# turtle.speed(5)
# # 控制画笔颜色
# turtle.pencolor('red')
# # 将画笔定位到原点
# turtle.goto(0,0)
# # 落笔
# turtle.pendown()
# # 从原点开始，画出一个边长为100的正方形
# for i in range(4):
#     # 正向运动 100 的距离
#     turtle.forward(200)
#     # 向右偏 90 度
#     turtle.right(90)
#
# # 完成正方形后起笔
# turtle.penup()
# # 将画笔定位到圆开始的位置
# turtle.goto(100,-200)
# # 落笔
# turtle.pendown()
# # 设置填充颜色
# turtle.fillcolor('blue')
# # 开始填充
# turtle.begin_fill()
# # 画出一个半径为100，占3/4的圆
# turtle.circle(100)
# # 结束填充
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(100,-100)
# turtle.write('Crossin编程教室')
# import random
# colors = ['red','blue','green','black','yellow','orange']
# for i in range(90):
#     turtle.setheading(i*4)
#     for i in range(4):
#         turtle.pencolor(random.choice(colors))
#         turtle.forward(100)
#         turtle.left(90)


# colors = ['red','blue','green','black','yellow','orange']
# i = 10
# for i in range(300):
#     turtle.pencolor(colors[i%6])
#     turtle.forward(i)
#     turtle.right(98)
#     # i += 1
#     turtle.forward(i+1)
#     turtle.right(119)
#     # i += 1
#     turtle.forward(i+1)
#     turtle.right(118)
#     i += 1

# # 控制画笔颜色
# turtle.pencolor('red')
# # 落笔
# turtle.pendown()
# # 设置填充颜色
# turtle.fillcolor('blue')
# # 开始填充
# turtle.begin_fill()
# # 从原点开始，画出一个边长为100的正方形
# for i in range(4):
#     # 正向运动 100 的距离
#     turtle.forward(200)
#     # 向右偏 90 度
#     turtle.right(90)
# # 结束填充
# turtle.end_fill()
# turtle.penup()
# turtle.goto(100,-100)
# turtle.write('Crossin编程教室')

turtle.color('red','red')
turtle.begin_fill()
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()



time.sleep(3)

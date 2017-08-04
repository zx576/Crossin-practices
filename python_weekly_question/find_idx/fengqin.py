import turtle

turtle.bgcolor('#0a173a')
t = turtle.Pen()
t.speed(9)

t.penup()

t.left(90)
t.back(250)
t.right(90)

t.pendown()

color = ['#D5D8E1', '#A22C28']
j = 1
radius = 250

for i in range(1, 7):

    if i % 2 == 1:
        t.pencolor(color[j % 2])
        t.fillcolor(color[j % 2])
        j += 1
    else:
        t.pencolor('#0A173A')
        t.fillcolor('#0A173A')

    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    t.left(90)

    t.penup()
    if i % 2 == 1:
        t.forward(40)
    else:
        t.forward(5)
    t.right(90)
    t.pendown()

    if i % 2 == 1:
        radius -= 40
    else:
        radius -= 5

t.penup()
t.left(90)
t.forward(150)
t.right(90)
t.back(110)

t.color('#D5D8E1')
t.begin_fill()
for i in range(5):
    t.forward(220)
    t.right(144)
t.end_fill()

t.forward(400)
t.pencolor('#0A173A')

turtle.done()
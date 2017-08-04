import turtle,time
t = turtle.Pen()
turtle.bgcolor('black')
co=['red','white','red','blue']
r=[48*5,38*5,28*5,18*5]
for i in range(4):
    t.color(co[i],co[i])
    t.begin_fill()
    t.circle(r[i])
    t.end_fill()
    t.up()
    t.left(90)
    if i < 3:
        t.forward(r[i]-r[i+1])
    else:
        t.forward(r[i]*2)
        t.right(90-18)
    t.right(90)
t.color(co[1], co[1])
t.begin_fill()
for i in range(5):
    t.forward(17*5*2)
    t.right(144)
t.end_fill()

turtle.done()
import turtle
pend = turtle.Turtle()
pend.speed("fast")
n = 70
turtle.bgcolor("white")

pend.pensize(3)
pend.pencolor("white")
for i in range(8):
    pend.forward(200)
    pend.back(200)
    pend.right(45)

pend.pencolor("red")
pend.pensize(3)
for i in range(8):
    pend.right(45)
    pend.circle(75)

pend.pencolor("black")
pend.pensize(2)
for i in range(8):
    pend.forward(200)
    pend.back(200)
    pend.right(45)

pend.forward(200)
pend.pencolor("red")
pend.right(90)
pend.pensize(4)
pend.forward(200)
for i in range(4):
    pend.right(90)
    pend.forward(400)
pend.pensize(3)

def draw_middlecircles():
    pend.right(225)
    pend.circle(90)
    pend.left(45)
    pend.forward(400)
    pend.left(45)
    pend.circle(90)
    pend.right(45)
    pend.left(90)
    pend.forward(400)
    pend.left(45)
    pend.circle(90)
    pend.left(45)
    pend.forward(400)
    pend.left(45)
    pend.circle(90)
    pend.left(45)
draw_middlecircles()

pend.pensize(2)
pend.pencolor("black")
for i in range(4):
    pend.forward(400)
    pend.left(90)

pend.penup()
pend.home()
pend.pencolor("white")
pend.pensize(1)
for i in range(8):
    pend.forward(200)
    pend.right(90)
    pend.pendown()
    pend.forward(250)
    pend.back(500)
    pend.forward(250)
    pend.left(90)
    pend.penup()
    pend.back(200)
    pend.right(45)

turtle.bgcolor("black")
pend.forward(200)
pend.left(135)

def draw_purplestuff():
    pend.pencolor("purple")
    pend.pensize(2)
    pend.pendown()
    pend.forward(340)
    pend.back(340)
    pend.left(90)
    pend.forward(340)
    pend.back(340)
    pend.right(45)
    pend.penup()
    pend.forward(400)
    pend.pendown()
    pend.right(135)
    pend.forward(340)
    pend.back(340)
    pend.right(90)
    pend.forward(340)
    pend.back(340)
    pend.right(135)
    pend.forward(150)
    pend.right(180)
    pend.penup()
    pend.forward(550)
    pend.pendown()
    pend.forward(150)
    pend.back(110)
    pend.right(90)
    pend.forward(275)
    pend.back(550)
    pend.right(90)
    pend.forward(480)
    pend.left(90)
    pend.forward(550)
    pend.left(90)
    pend.forward(480)
draw_purplestuff()


turtle.hideturtle()
turtle.done()
import turtle

tina = turtle.Turtle(shape='turtle')
scr = turtle.Screen()
scr.bgcolor("white")

tina.pensize(3)
tina.pencolor("brown")

def sechseck(farbe, seitenLaenge):
    tina.penup()
    tina.forward(seitenLaenge)
    tina.right(120)

    tina.pendown()
    tina.fillcolor(farbe)
    tina.begin_fill()
    for _ in range(6):
        tina.forward(seitenLaenge)
        tina.right(60)
    tina.end_fill()
    tina.penup()

    tina.right(60)
    tina.forward(seitenLaenge)
    tina.right(180)


tina.left(90)
sechseck("yellow", 100)

tina.forward(100)
tina.right(60)
tina.forward(100)
tina.right(60)

for _ in range(6):
    sechseck("orange", 100)
    tina.forward(100)
    tina.right(60)
    tina.forward(100)

scr.exitonclick()
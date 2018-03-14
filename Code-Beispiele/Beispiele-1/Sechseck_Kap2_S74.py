import turtle

tina = turtle.Turtle(shape='turtle')
scr = turtle.Screen()
scr.bgcolor("white")

tina.pensize(3)

seitenLaenge = 100

tina.left(90)
tina.penup()
tina.forward(seitenLaenge)
tina.right(120)

tina.pendown()
for _ in range(6):
    tina.forward(seitenLaenge)
    tina.right(60)

tina.penup()
tina.right(60)
tina.forward(seitenLaenge)
tina.right(180)

scr.exitonclick()
# Eyes Kap2 Seite 71

import turtle

tina = turtle.Turtle(shape='turtle')
scr = turtle.Screen()
scr.bgcolor("white")

tina.left(90)


tina.pensize(3)
tina.circle(80)
tina.circle(-80)

tina.pensize(5)
tina.circle(40)
tina.circle(-40)

tina.pensize(7)
tina.circle(120,75)
tina.penup()
tina.circle(120,-75)
tina.pendown()
tina.circle(-120,75)
tina.penup()
tina.circle(-120,-75)

scr.exitonclick()
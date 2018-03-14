# 3 gleichseitige, gefüllte Dreiecke

import turtle

tina = turtle.Turtle(shape='turtle')
scr = turtle.Screen()
scr.bgcolor("white")

tina.pensize(5)

# Dreieck 1
tina.pencolor("red")
tina.fillcolor("cyan")
tina.begin_fill()
tina.forward(135)
tina.left(120)
tina.forward(135)
tina.left(120)
tina.forward(135)
tina.left(120)
tina.end_fill()

tina.left(120)

# Dreieck 2
tina.pencolor("green")
tina.fillcolor("magenta")
tina.begin_fill()
tina.forward(135)
tina.left(120)
tina.forward(135)
tina.left(120)
tina.forward(135)
tina.left(120)
tina.end_fill()

tina.left(120)

#  Dreieick 3
tina.pencolor("blue")
tina.fillcolor("yellow")
tina.begin_fill()
tina.forward(135)
tina.left(120)
tina.forward(135)
tina.left(120)
tina.forward(135)
tina.left(120)
tina.end_fill()

scr.exitonclick()
# Haus mit Dach

import turtle

tina = turtle.Turtle(shape='turtle')
scr = turtle.Screen()
scr.bgcolor("white")

hausBreite = 100
hausHoehe = 60
dachBreite = 140

# Haus
tina.pensize(2)

tina.forward(hausBreite)
tina.right(90)
tina.forward(hausHoehe)
tina.right(90)
tina.forward(hausBreite)
tina.right(90)
tina.forward(hausHoehe)

# Dach
tina.pensize(5)

tina.left(90)
tina.forward((dachBreite - hausBreite) / 2)
tina.right(120)
tina.forward(dachBreite)
tina.right(120)
tina.forward(dachBreite)
tina.right(120)
tina.forward(dachBreite)

scr.exitonclick()
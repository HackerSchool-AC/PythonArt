# 4 kreise ineinander in unterschiedlichen Farben
# Step 2: Variablen für Winkel, Seitenlänge und Farbe

import turtle

tina = turtle.Turtle(shape='turtle')
scr = turtle.Screen()
scr.bgcolor("white")

tina.penup()
tina.goto(0, -270)
tina.pendown()

radius = 350
x = 255/255.
y = 0/255.

def kreis(radius, farbe):
    tina.pencolor(farbe)
    tina.fillcolor(farbe)
    tina.begin_fill()
    tina.circle(radius)
    tina.end_fill()

# kreis 1
radius = radius - 75
farbe = (x, x, y)
kreis(radius, farbe)

# kreis 2
radius = radius - 75
farbe = (y, x, y)
kreis(radius, farbe)

# kreis 3
radius = radius - 75
farbe = (x, y, y)
kreis(radius, farbe)

# kreis 4
radius = radius - 75
farbe = (x, y, x)
kreis(radius, farbe)
tina.end_fill()


scr.exitonclick()
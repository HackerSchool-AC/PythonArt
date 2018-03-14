# 4 Quadrate ineinander in unterschiedlichen Farben
# Step 2: Variablen für Winkel, Seitenlänge und Farbe

import turtle

tina = turtle.Turtle(shape='turtle')
scr = turtle.Screen()
scr.bgcolor("white")

tina.penup()
tina.goto(-150, -150)
tina.pendown()

seite = 375
winkel = 90
x = 255/255.
y = 0/255.

# Quadrat 1
seite = seite - 75
farbe = (x, x, y)
tina.pencolor(farbe)
tina.fillcolor(farbe)
tina.begin_fill()
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.end_fill()

# Quadrat 2
seite = seite - 75
farbe = (y, x, y)
tina.pencolor(farbe)
tina.fillcolor(farbe)
tina.begin_fill()
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.end_fill()

# Quadrat 3
seite = seite - 75
farbe = (x, y, y)
tina.pencolor(farbe)
tina.fillcolor(farbe)
tina.begin_fill()
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.end_fill()

# Quadrat 4
seite = seite - 75
farbe = (x, y, x)
tina.pencolor(farbe)
tina.fillcolor(farbe)
tina.begin_fill()
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.forward(seite)
tina.left(winkel)
tina.end_fill()


scr.exitonclick()
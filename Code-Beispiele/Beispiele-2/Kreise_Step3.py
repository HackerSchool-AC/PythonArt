# 4 kreise ineinander in unterschiedlichen Farben
# Step 2: Variablen für Winkel, Seitenlänge und Farbe

from turtle import *

shape("turtle")

Screen().bgcolor("white")

penup()
goto(0, -270)
pendown()

radius = 350
x = 255/255.
y = 0/255.

def kreis(radius, farbe):
    pencolor(farbe)
    fillcolor(farbe)
    begin_fill()
    circle(radius)
    end_fill()

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
end_fill()


Screen().exitonclick()
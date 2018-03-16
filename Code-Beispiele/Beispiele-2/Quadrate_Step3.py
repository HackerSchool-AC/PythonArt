# 4 Quadrate ineinander in unterschiedlichen Farben
# Step 2: Variablen für Winkel, Seitenlänge und Farbe

from turtle import *

shape("turtle")

Screen().bgcolor("white")

penup()
goto(-150, -150)
pendown()

seite = 375
winkel = 90
x = 255/255.
y = 0/255.

def quadrat(seite, farbe):
    pencolor(farbe)
    fillcolor(farbe)
    begin_fill()
    forward(seite)
    left(winkel)
    forward(seite)
    left(winkel)
    forward(seite)
    left(winkel)
    forward(seite)
    left(winkel)
    end_fill()

# Quadrat 1
seite = seite - 75
farbe = (x, x, y)
quadrat(seite, farbe)

# Quadrat 2
seite = seite - 75
farbe = (y, x, y)
quadrat(seite, farbe)

# Quadrat 3
seite = seite - 75
farbe = (x, y, y)
quadrat(seite, farbe)

# Quadrat 4
seite = seite - 75
farbe = (x, y, x)
quadrat(seite, farbe)
end_fill()


Screen().exitonclick()
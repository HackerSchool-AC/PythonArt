from turtle import *

shape("turtle")
tracer(False)

def quadrat(seite, farbe):
    pos = position()
    penup()

    forward(seite / 2)
    right(90)
    forward(seite / 2)

    fillcolor(farbe)
    begin_fill()
    pensize(2)
    pendown()
    for i in range(4):
        right(90)
        forward(seite)
    end_fill()

    penup()
    setposition(pos)

seite = numinput("Quadrate", "Wie groß soll das größte Quadrat sein?")

while seite > 10:
    quadrat(seite, "red")
    seite = seite - 20

Screen().exitonclick()
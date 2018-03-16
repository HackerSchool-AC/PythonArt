from turtle import *
import random

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
aenderung = numinput("Quadrate", "Wie viel kleiner sollen die Quadrate werden?")


while seite > 10:
    quadrat(seite, random.choice(["red", "blue", "yellow", "green"]))
    seite = seite - aenderung
    right(random.randint(0, 90))

Screen().exitonclick()
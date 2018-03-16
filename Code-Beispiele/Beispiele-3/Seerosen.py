import random
from turtle import *

Screen().bgcolor("blue")

shape("turtle")
tracer(False)

def rotesQuadrat(seite):
    pos = position()
    penup()

    forward(seite / 2)
    right(90)
    forward(seite / 2)

    fillcolor("red")
    begin_fill()
    pensize(2)
    pendown()
    for i in range(4):
        right(90)
        forward(seite)
    end_fill()

    penup()
    setposition(pos)

def rosenBluete(groesse):
    seite = groesse
    while seite > 10:
        right(random.randint(0, 360))
        rotesQuadrat(seite)
        seite = seite - 5

def blatt(radius):
    pos = position()
    penup()

    forward(radius)
    left(90)
    fillcolor("green")
    pensize(2)
    pendown()
    begin_fill()
    circle(radius)
    end_fill()

    penup()
    setposition(pos)

def seerose(groesse):
    blatt(0.8 * groesse)
    rosenBluete(groesse)

anzahl = numinput("Seerosenteich", "Wie viele Seerosen?")

for i in range(int(anzahl)):
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)

    penup()
    goto(x, y)
    seerose(random.randint(80, 120))

Screen().exitonclick()
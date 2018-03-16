import random
from turtle import *

shape("turtle")

def quadrat(seite, farbe):
    fillcolor(farbe)
    begin_fill()
    for _ in range(4):
        forward(seite)
        right(90)
    end_fill()

def farbeZufall():
    farben = ["red", "blue", "yellow", "green", "brown", "pink"]
    return random.choice(farben)

def zeichneQuadrate(anzahl, seite):
    if anzahl > 0:
        quadrat(seite, farbeZufall())
        penup()
        left(90)
        forward(seite * 0.3)
        left(90)
        forward(seite * 0.3)
        left(180)
        pendown()
        left(10)
        zeichneQuadrate(anzahl - 1, seite * 0.95)

zeichneQuadrate(50, 200)

Screen().exitonclick()
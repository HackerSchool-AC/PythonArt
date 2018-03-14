import random
import turtle

tina = turtle.Turtle(shape="turtle")

def quadrat(seite, farbe):
    tina.fillcolor(farbe)
    tina.begin_fill()
    for _ in range(4):
        tina.forward(seite)
        tina.right(90)
    tina.end_fill()

def farbeZufall():
    farben = ["red", "blue", "yellow", "green", "brown", "pink"]
    return random.choice(farben)

def zeichneQuadrate(anzahl, seite):
    if anzahl > 0:
        quadrat(seite, farbeZufall())
        tina.penup()
        tina.left(90)
        tina.forward(seite * 0.3)
        tina.left(90)
        tina.forward(seite * 0.3)
        tina.left(180)
        tina.pendown()
        tina.left(10)
        zeichneQuadrate(anzahl - 1, seite * 0.95)

zeichneQuadrate(50, 200)

turtle.Screen().exitonclick()
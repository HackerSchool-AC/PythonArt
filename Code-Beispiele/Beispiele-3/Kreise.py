from turtle import *
import random

shape("turtle")
tracer(False)

def kreis(radius, farbe):
    penup()

    forward(radius)
    left(90)
    fillcolor(farbe)
    begin_fill()
    pensize(2)
    pendown()
    circle(radius)
    end_fill()

r = 400

while r > 10:
    penup()
    goto(0, 0)
    kreis(r, random.choice(["red", "blue", "yellow", "green"]))
    r = r - 20

Screen().exitonclick()
from turtle import *
import random

shape("turtle")
tracer(False)

def yin(radius, farbe1, farbe2):
    pendown()
    fillcolor(farbe1)
    begin_fill()
    circle(radius / 2, 180)
    circle(radius, 180)
    left(180)
    circle(-radius / 2, 180)
    end_fill()
    penup()

    left(90)
    forward(radius / 2)
    dot(radius / 4, farbe2)
    right(180)
    forward(radius / 2)
    left(90)

def yinyang(radius):
    pensize(3)
    pencolor("black")
    pendown()
    yin(radius, "black", "white")
    left(180)
    yin(radius, "white", "black")

yinyang(200)

Screen().exitonclick()
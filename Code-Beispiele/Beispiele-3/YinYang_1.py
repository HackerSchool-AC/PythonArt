from turtle import *
import random

shape("turtle")
tracer(False)

def yin(radius, farbe):
    fillcolor(farbe)
    begin_fill()
    circle(radius / 2, 180)
    circle(radius, 180)
    left(180)
    circle(-radius / 2, 180)
    end_fill()

def yinyang(radius):
    pensize(3)
    pencolor("black")
    pendown()
    yin(radius, "black")
    left(180)
    yin(radius, "white")

yinyang(200)

Screen().exitonclick()
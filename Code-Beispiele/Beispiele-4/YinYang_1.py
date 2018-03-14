import turtle
import random

tina = turtle.Turtle(shape="turtle")
turtle.tracer(False)

def yin(radius, farbe):
    tina.fillcolor(farbe)
    tina.begin_fill()
    tina.circle(radius / 2, 180)
    tina.circle(radius, 180)
    tina.left(180)
    tina.circle(-radius / 2, 180)
    tina.end_fill()

def yinyang(radius):
    tina.pensize(3)
    tina.pencolor("black")
    tina.pendown()
    yin(radius, "black")
    tina.left(180)
    yin(radius, "white")

yinyang(200)

turtle.Screen().exitonclick()
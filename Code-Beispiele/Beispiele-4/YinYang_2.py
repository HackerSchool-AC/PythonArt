import turtle
import random

tina = turtle.Turtle(shape="turtle")
turtle.tracer(False)

def yin(radius, farbe1, farbe2):
    tina.pendown()
    tina.fillcolor(farbe1)
    tina.begin_fill()
    tina.circle(radius / 2, 180)
    tina.circle(radius, 180)
    tina.left(180)
    tina.circle(-radius / 2, 180)
    tina.end_fill()
    tina.penup()

    tina.left(90)
    tina.forward(radius / 2)
    tina.dot(radius / 4, farbe2)
    tina.right(180)
    tina.forward(radius / 2)
    tina.left(90)

def yinyang(radius):
    tina.pensize(3)
    tina.pencolor("black")
    tina.pendown()
    yin(radius, "black", "white")
    tina.left(180)
    yin(radius, "white", "black")

yinyang(200)

turtle.Screen().exitonclick()
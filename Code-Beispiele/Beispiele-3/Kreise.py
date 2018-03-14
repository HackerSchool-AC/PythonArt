import turtle
import random

tina = turtle.Turtle(shape="turtle")
turtle.tracer(False)

def kreis(radius, farbe):
    tina.penup()

    tina.forward(radius)
    tina.left(90)
    tina.fillcolor(farbe)
    tina.begin_fill()
    tina.pensize(2)
    tina.pendown()
    tina.circle(radius)
    tina.end_fill()

r = 400

while r > 10:
    tina.penup()
    tina.goto(0, 0)
    kreis(r, random.choice(["red", "blue", "yellow", "green"]))
    r = r - 20

turtle.Screen().exitonclick()
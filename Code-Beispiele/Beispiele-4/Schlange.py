from turtle import *

tina = Turtle(shape = "turtle")
tracer(False)

def maleSchlange(radius, dicke, winkel, boegen, farbe):
    pendown()
    pensize(dicke)
    pencolor(farbe)

    for i in range(boegen):
        circle(radius, winkel)
        circle(-radius, winkel)

maleSchlange(80, 40, 60, 3, "green")
left(180)
maleSchlange(80, 10, 60, 3, "brown")
pencolor("green")
pensize(100)
pendown()
forward(300)

Screen().exitonclick()


from turtle import *

shape("turtle")

Screen().bgcolor("white")

pensize(3)
pencolor("brown")

def sechseck(farbe, seitenLaenge):
    penup()
    forward(seitenLaenge)
    right(120)

    pendown()
    fillcolor(farbe)
    begin_fill()
    for _ in range(6):
        forward(seitenLaenge)
        right(60)
    end_fill()
    penup()

    right(60)
    forward(seitenLaenge)
    right(180)


left(90)
sechseck("yellow", 100)

forward(100)
right(60)
forward(100)
right(60)

for _ in range(6):
    sechseck("orange", 100)
    forward(100)
    right(60)
    forward(100)

Screen().exitonclick()
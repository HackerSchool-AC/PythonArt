from turtle import *

shape("turtle")

Screen().bgcolor("white")

pensize(3)

seitenLaenge = 100

left(90)
penup()
forward(seitenLaenge)
right(120)

pendown()
for _ in range(6):
    forward(seitenLaenge)
    right(60)

penup()
right(60)
forward(seitenLaenge)
right(180)

Screen().exitonclick()
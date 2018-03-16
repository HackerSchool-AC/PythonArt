# Eyes Kap2 Seite 71

from turtle import *

shape("turtle")

Screen().bgcolor("white")

left(90)


pensize(3)
circle(80)
circle(-80)

pensize(5)
circle(40)
circle(-40)

pensize(7)
circle(120,75)
penup()
circle(120,-75)
pendown()
circle(-120,75)
penup()
circle(-120,-75)

Screen().exitonclick()
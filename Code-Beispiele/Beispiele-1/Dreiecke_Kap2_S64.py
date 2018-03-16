# 3 gleichseitige, gefüllte Dreiecke

from turtle import *

shape("turtle")

Screen().bgcolor("white")

pensize(5)

# Dreieck 1
pencolor("red")
fillcolor("cyan")
begin_fill()
forward(135)
left(120)
forward(135)
left(120)
forward(135)
left(120)
end_fill()

left(120)

# Dreieck 2
pencolor("green")
fillcolor("magenta")
begin_fill()
forward(135)
left(120)
forward(135)
left(120)
forward(135)
left(120)
end_fill()

left(120)

#  Dreieick 3
pencolor("blue")
fillcolor("yellow")
begin_fill()
forward(135)
left(120)
forward(135)
left(120)
forward(135)
left(120)
end_fill()

Screen().exitonclick()
# Haus mit Dach

from turtle import *

shape("turtle")

Screen().bgcolor("white")

hausBreite = 100
hausHoehe = 60
dachBreite = 140

# Haus
pensize(2)

forward(hausBreite)
right(90)
forward(hausHoehe)
right(90)
forward(hausBreite)
right(90)
forward(hausHoehe)

# Dach
pensize(5)

left(90)
forward((dachBreite - hausBreite) / 2)
right(120)
forward(dachBreite)
right(120)
forward(dachBreite)
right(120)
forward(dachBreite)

Screen().exitonclick()
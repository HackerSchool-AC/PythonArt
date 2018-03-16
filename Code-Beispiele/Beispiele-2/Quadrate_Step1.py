# 4 Quadrate ineinander in unterschiedlichen Farben
# Step 1: iterativ

from turtle import *

shape("turtle")

Screen().bgcolor("white")

penup()
goto(-150, -150)
pendown()

# Quadrat 1
# Seite = 300
# Farbe = (255, 255, 0)
pencolor(255/255., 255/255., 0/255.)
fillcolor(255/255., 255/255., 0/255.)
begin_fill()
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
end_fill()

# Quadrat 2
# Seite = 225
# Farbe = (0, 255, 0)
pencolor(0/255., 255/255., 0/255.)
fillcolor(0/255., 255/255., 0/255.)
begin_fill()
forward(225)
left(90)
forward(225)
left(90)
forward(225)
left(90)
forward(225)
left(90)
end_fill()

# Quadrat 3
# Seite = 150
# Farbe = (255, 0, 0)
pencolor(255/255., 0/255., 0/255.)
fillcolor(255/255., 0/255., 0/255.)
begin_fill()
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
end_fill()

# Quadrat 4
# Seite = 75
# Farbe = (255, 0, 255)
pencolor(255/255., 0/255., 255/255.)
fillcolor(255/255., 0/255., 255/255.)
begin_fill()
forward(75)
left(90)
forward(75)
left(90)
forward(75)
left(90)
forward(75)
left(90)
end_fill()


Screen().exitonclick()

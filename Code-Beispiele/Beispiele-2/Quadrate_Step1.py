# 4 Quadrate ineinander in unterschiedlichen Farben
# Step 1: iterativ

import turtle

tina = turtle.Turtle(shape='turtle')
scr = turtle.Screen()
scr.bgcolor("white")

tina.penup()
tina.goto(-150, -150)
tina.pendown()

# Quadrat 1
# Seite = 300
# Farbe = (255, 255, 0)
tina.pencolor(255/255., 255/255., 0/255.)
tina.fillcolor(255/255., 255/255., 0/255.)
tina.begin_fill()
tina.forward(300)
tina.left(90)
tina.forward(300)
tina.left(90)
tina.forward(300)
tina.left(90)
tina.forward(300)
tina.left(90)
tina.end_fill()

# Quadrat 2
# Seite = 225
# Farbe = (0, 255, 0)
tina.pencolor(0/255., 255/255., 0/255.)
tina.fillcolor(0/255., 255/255., 0/255.)
tina.begin_fill()
tina.forward(225)
tina.left(90)
tina.forward(225)
tina.left(90)
tina.forward(225)
tina.left(90)
tina.forward(225)
tina.left(90)
tina.end_fill()

# Quadrat 3
# Seite = 150
# Farbe = (255, 0, 0)
tina.pencolor(255/255., 0/255., 0/255.)
tina.fillcolor(255/255., 0/255., 0/255.)
tina.begin_fill()
tina.forward(150)
tina.left(90)
tina.forward(150)
tina.left(90)
tina.forward(150)
tina.left(90)
tina.forward(150)
tina.left(90)
tina.end_fill()

# Quadrat 4
# Seite = 75
# Farbe = (255, 0, 255)
tina.pencolor(255/255., 0/255., 255/255.)
tina.fillcolor(255/255., 0/255., 255/255.)
tina.begin_fill()
tina.forward(75)
tina.left(90)
tina.forward(75)
tina.left(90)
tina.forward(75)
tina.left(90)
tina.forward(75)
tina.left(90)
tina.end_fill()


scr.exitonclick()

import turtle

tina = turtle.Turtle(shape = "turtle")
#turtle.tracer(False)

tina.left(90)

tina.penup()
tina.back(25)
tina.right(90)
tina.back(60)
tina.pendown()

# Wand
tina.pensize(3)
tina.forward(120)
tina.right(90)
tina.forward(70)
tina.right(90)
tina.forward(120)
tina.right(90)
tina.forward(70)
tina.right(90)

tina.penup()
tina.back(15)
tina.pendown()

# Dach
tina.pensize(5)
tina.pencolor("red")
tina.forward(150)
tina.left(120)
tina.forward(150)
tina.left(120)
tina.forward(150)
tina.left(120)

turtle.Screen().exitonclick()
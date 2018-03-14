import turtle

tina = turtle.Turtle(shape = "turtle")
turtle.tracer(False)

def maleSchlange(radius, dicke, winkel, boegen, farbe):
    tina.pendown()
    tina.pensize(dicke)
    tina.pencolor(farbe)

    for i in range(boegen):
        tina.circle(radius, winkel)
        tina.circle(-radius, winkel)

maleSchlange(80, 40, 60, 3, "green")
tina.left(180)
maleSchlange(80, 10, 60, 3, "brown")
tina.pencolor("green")
tina.pensize(100)
tina.pendown()
tina.forward(300)

turtle.Screen().exitonclick()


import turtle

tina = turtle.Turtle(shape = "turtle")
# turtle.tracer(False)

def maleKreis(radius, farbe):
    # Gehe zum Rand
    tina.forward(radius)
    tina.left(90)

    # Male den Kreis

    tina.pendown()
    tina.pensize(2)
    tina.fillcolor(farbe)
    tina.begin_fill()

    tina.circle(radius)

    tina.end_fill()

def maleSechseck(seite, farbe):
    # Gehe zum Rand
    tina.forward(seite)
    tina.left(120)

    # Male das Sechseck

    tina.pendown()
    tina.pensize(2)
    tina.fillcolor(farbe)
    tina.begin_fill()

    for i in range(6):
        tina.forward(seite)
        tina.left(60)

    tina.end_fill()


# Gehe zur Mitte
tina.penup()
tina.goto(0, 0)

maleKreis(300, "red")

# Gehe zur Mitte
tina.penup()
tina.goto(0, 0)

maleSechseck(300, "blue")


turtle.Screen().exitonclick()


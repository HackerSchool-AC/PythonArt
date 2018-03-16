from turtle import *

tina = Turtle(shape = "turtle")
# tracer(False)

def maleKreis(radius, farbe):
    # Gehe zum Rand
    forward(radius)
    left(90)

    # Male den Kreis

    pendown()
    pensize(2)
    fillcolor(farbe)
    begin_fill()

    circle(radius)

    end_fill()

def maleSechseck(seite, farbe):
    # Gehe zum Rand
    forward(seite)
    left(120)

    # Male das Sechseck

    pendown()
    pensize(2)
    fillcolor(farbe)
    begin_fill()

    for i in range(6):
        forward(seite)
        left(60)

    end_fill()


# Gehe zur Mitte
penup()
goto(0, 0)

maleKreis(300, "red")

# Gehe zur Mitte
penup()
goto(0, 0)

maleSechseck(300, "blue")


Screen().exitonclick()


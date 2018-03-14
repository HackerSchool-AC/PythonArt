import turtle

tina = turtle.Turtle(shape="turtle")
turtle.tracer(False)

def quadrat(seite, farbe):
    position = tina.position()
    tina.penup()

    tina.forward(seite / 2)
    tina.right(90)
    tina.forward(seite / 2)

    tina.fillcolor(farbe)
    tina.begin_fill()
    tina.pensize(2)
    tina.pendown()
    for i in range(4):
        tina.right(90)
        tina.forward(seite)
    tina.end_fill()

    tina.penup()
    tina.setposition(position)

seite = turtle.numinput("Quadrate", "Wie groß soll das größte Quadrat sein?")
aenderung = turtle.numinput("Quadrate", "Wie viel kleiner sollen die Quadrate werden?")
winkel = turtle.numinput("Quadrate", "Um welchen Winkel sollen die Quadrate gedreht werden?")

while seite > 10:
    quadrat(seite, "red")
    seite = seite - aenderung
    tina.right(winkel)

turtle.Screen().exitonclick()
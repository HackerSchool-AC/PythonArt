import random
import turtle

turtle.Screen().bgcolor("blue")

tina = turtle.Turtle(shape="turtle")
turtle.tracer(False)

def rotesQuadrat(seite):
    position = tina.position()
    tina.penup()

    tina.forward(seite / 2)
    tina.right(90)
    tina.forward(seite / 2)

    tina.fillcolor("red")
    tina.begin_fill()
    tina.pensize(2)
    tina.pendown()
    for i in range(4):
        tina.right(90)
        tina.forward(seite)
    tina.end_fill()

    tina.penup()
    tina.setposition(position)

def rosenBluete(groesse):
    seite = groesse
    while seite > 10:
        tina.right(random.randint(0, 360))
        rotesQuadrat(seite)
        seite = seite - 5

def blatt(radius):
    position = tina.position()
    tina.penup()

    tina.forward(radius)
    tina.left(90)
    tina.fillcolor("green")
    tina.pensize(2)
    tina.pendown()
    tina.begin_fill()
    tina.circle(radius)
    tina.end_fill()

    tina.penup()
    tina.setposition(position)

def seerose(groesse):
    blatt(0.8 * groesse)
    rosenBluete(groesse)

anzahl = turtle.numinput("Seerosenteich", "Wie viele Seerosen?")

for i in range(int(anzahl)):
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)

    tina.penup()
    tina.goto(x, y)
    seerose(random.randint(80, 120))

turtle.Screen().exitonclick()

canvasvg.saveall("Seerosen.svg", turtle.Screen().getcanvas())
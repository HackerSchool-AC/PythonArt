Funktionen des Moduls "turtle" in Python
======
Für das Zeichnen mit Python und dem Modul "turtle" ist es notwendig einige Funktionen zu
kennen. Welche das sind, wie man diese programmiert und welche Parameter man einstellen muss könnt ihr hier nachlesen. In dieser Zusammenfassung werden jedoch nur die Funktionen aufgelistet, die wir in dem Kurs nutzen. 

Weitere Funktionen findet ihr auf dieser Webseite (in englisch):

https://docs.python.org/3.5/library/turtle.html
 

Turtle Bewegungen
======

Es ist wichtig daran zu denken, dass die Turtle sich immer in die Richtung bewegt, in die sie zeigt.

Bewegen und zeichnen
--------

**forward(distance)**  
Die Turtle bewegt sich um die Strecke *distance* (in Pixel) vorwärts. 

**backward(distance)**  
Die Turtle bewegt sich um die Strecke *distance* (in Pixel) rückwärts. 

**left(angle)**  
Die Turtle dreht sich um den Winkel *angle* nach links. 

**right(angel)**  
Die Turtle dreht sich um den Winkel *angle* nach rechts. 

**goto(x, y)**  
Die Turtle bewegt sich zur Koordinate *(x,y)*. Wenn der Stift unten ist, wird eine Strecke gezeichnet. Die Orientierung der Turtle ändert sich nicht. 

**circle(radius, extent)**  
Die Turtle zeichnet einen Kreis(bogen) mit dem Radius *radius*. Der Winkel *extent* gibt an, welcher Teil des Kreises gezeichnet werden soll. Wenn *extent* fehlt wird ein voller Kreis gezeichnet. 

Steuerung des Stiftes
=======

**pendown()**  
Setzt den Zeichenstift nach unten und malt bei jeder weiteren Bewegung. 

**penup()**  
Hebt den Zeichenstift an. Es wird nicht gezeichnet, wenn der Turtle sich bewegt 

**pensize(width)**  
Setzt die Strichdicke auf *width* Pixel

**pencolor(color)**  
Setzt die Füllfarbe mit der Farbe *color*

**fillcolor(color)**  
Setzt die Zeichenfarbe mit der Farbe *color*

**begin_fill()**  
Beginnt das Zeichen einer Figur, die gefüllt werden soll.

**end_fill()**  
Füllt die Figur, die nach dem Aufruf von *begin_fill* gezeichnet wurde. Die Füllfarbe wird mit der Funktion *fillcolor* gesetzt.


Zustand der Turtle
=======

**shape(name)**  
Setzt die Gestalt der Turtle auf die Gestalt mit dem Namen *name*. Es sind möglich: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”

Weitere nützliche Funktionen
=======

**tracer(flag)**  
Schaltet die Turtle-Animationen ein, wenn *flag*=*TRUE*, bzw. aus, wenn *flag*=*FALSE*.

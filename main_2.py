import turtle
t = turtle.Pen()
t.shape("turtle")
t.hideturtle()
t.speed(5)

def huegel():
    t.penup()
    t.home()
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(180)
    t.pendown()
    t.circle(50,180)
    t.right(90)
    t.penup()
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.pendown()

def Boden():
    t.penup()
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(400)
    t.left(180)
    t.pendown()
    t.forward(800)

def senkrechte():
    t.forward(150)
    t.right(90)


def waagerechte():
    t.forward(100)
    t.right(90)

def senkrechte2():
    t.forward(20)
    t.penup()
    t.right(90)
    t.pendown()


def Kreis():
    t.circle(15)
    t.penup()
    t.left(90)
    t.forward(30)
    t.pendown()

def Senkrechte3():
    t.pendown()
    t.forward(50)


def Arme():
    t.right(180)
    t.forward(30)
    t.right(135)
    t.forward(20)
    t.right(180)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(180)
    t.forward(20)
    t.right(135)


def Beine():
    t.forward(50)
    t.right(35)
    t.forward(40)
    t.right(180)
    t.forward(40)
    t.right(110)
    t.fd(40)
    t.right(180)

zeichenliste = [Boden, huegel, senkrechte, waagerechte, senkrechte2, Kreis, Senkrechte3, Arme, Beine]


schritte = [Boden, huegel, senkrechte, waagerechte, senkrechte2, Kreis, Senkrechte3, Arme, Beine]

import random
import turtle
import wortliste

# Zufälliges Wort auswählen
wort = random.choice(wortliste.wörter)

# Turtle-Objekt erstellen
s = turtle.Pen()
s.hideturtle()

def drawlines(geratenes):
  s.clear()
  s.penup()
  s.goto(-100, 80)
  s.pendown()
  for buchstabe in wort:
    s.pendown()
    s.forward(10)
    if buchstabe in geratenes:
      s.write(buchstabe, align="center", font="arial 12 bold")
    s.forward(10)
    s.penup()
    s.forward(20)
    s.pendown()

gefunden = ""

# Initialer Aufruf von drawlines, um die Anzahl der Buchstaben anzuzeigen
drawlines(gefunden)

for schritt in schritte:
  buchstabe = turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?") or ""
  while buchstabe.lower() in wort or buchstabe.upper() in wort:
    gefunden = gefunden + buchstabe.lower() + buchstabe.upper()
    drawlines(gefunden)
    buchstabe = turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?") or ""
  else:
    schritt()



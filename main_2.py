import turtle
from turtle import*
shape("turtle")
hideturtle()
speed(5)


def huegel():
    penup()
    home()
    pendown()
    left(90)
    penup()
    backward(200)
    pendown()
    circle(100,180)
    right(90)
    penup()
    backward(100)
    right(90)
    forward(100)
    pendown()


def Boden():
    penup()
    right(90)
    forward(200)
    left(90)
    forward(400)
    left(180)
    pendown()
    forward(800)

def senkrechte():
    forward(250)
    right(90)

def waagerechte():
    forward(300)
    right(90)

def senkrechte2():
    forward(50)
    penup()
    right(90)
    pendown()

def Kreis():
    circle(35)
    penup()
    left(90)
    forward(70)
    pendown()

def Senkrechte3():
    forward(100)

def Arme():
    right(180)
    forward(70)
    right(135)
    forward(40)
    right(180)
    forward(40)
    left(90)
    forward(40)
    right(180)
    forward(40)
    right(135)

def Beine():
    forward(70)
    right(35)
    forward(90)
    right(180)
    forward(90)
    right(110)
    fd(90)
    right(180)

print(Boden())
print(huegel())
print(senkrechte())
print(waagerechte())
print(senkrechte2())
print(Kreis())
print(Senkrechte3())
print(Arme())
print(Beine())


schritte = [Boden, huegel, senkrechte, waagerechte, senkrechte2, Kreis, Senkrechte3, Arme, Beine]

for schritt in schritte:
    turtle.textinput("Hangman", "Welchen Buchstaben wählen Sie?")

    
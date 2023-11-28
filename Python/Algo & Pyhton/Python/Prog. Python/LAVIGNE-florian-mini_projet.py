# Florian Lavigne

from turtle import *

# Question 1
# Question 1a : Il y a une erreur parce que les fonctions ne sont pas définies. (NameError: name 'forward' is not defined)
# Question 1b : La ligne que l'on a ajouté, sert à importer l'entièreté de la librairie "turtle".

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
exitonclick()

# Question 2
turtle = Turtle()
rayon = 50
turtle.circle(rayon)
turtle.penup()
turtle.goto (0, -100)
turtle.pendown()
turtle.circle(rayon)
turtle.penup()
turtle.goto (100, 0)
turtle.pendown()
turtle.circle(rayon)
turtle.penup()
turtle.goto (100, -100)
turtle.pendown()
turtle.circle(rayon)
turtle.hideturtle()
exitonclick()

# Question 3
turtle = Turtle()
rayon = int(input("Ecriver la valeur du rayon :"))
for i in range(rayon) :
    turtle.circle(rayon)
    turtle.penup()
    turtle.goto (0, - 2* rayon)
    turtle.pendown()
    turtle.circle(rayon)
    turtle.penup()
    turtle.goto (2*rayon, 0)
    turtle.pendown()
    turtle.circle(rayon)
    turtle.penup()
    turtle.goto (2*rayon, -2*rayon)
    turtle.pendown()
    turtle.circle(rayon)
    turtle.hideturtle()
exitonclick()

# Question 4
turtle = Turtle()
rayon = int(input("Ecriver la valeur du rayon :"))
turtle.color(input("Ecriver une couleur en anglais :"))
for i in range(rayon) :
    turtle.begin_fill()
    turtle.circle(rayon)
    turtle.end_fill()
    turtle.penup()
    turtle.goto (0, -2* rayon)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(rayon)
    turtle.end_fill()
    turtle.penup()
    turtle.goto (2*rayon, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(rayon)
    turtle.end_fill()
    turtle.penup()
    turtle.goto (2*rayon, -2*rayon)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(rayon)
    turtle.end_fill()
    turtle.hideturtle()
    exitonclick()
turtle.done()

# Question Bonus
turtle = Turtle()
size = 7
for i in range(23):
    turtle.forward(i * 7)
    turtle.right(90)
turtle.hideturtle()
exitonclick()
turtle.done()

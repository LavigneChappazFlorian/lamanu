from turtle import *
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

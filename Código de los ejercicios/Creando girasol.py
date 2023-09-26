# Importamos la libreria de math
import math

# Importamos la librería turtle
import turtle
from turtle import onkeypress, bye, done, listen

# Definimos la función para dibujar una estrella
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")

# Definimos la función para dibujar una estrella
phi = 137.508 * (math.pi / 180.0)

# Creamos un bucle para dibujar 100 estrellas
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    # Dibujamos la estrella
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()

    # Creamos una condición para dibujar una estrella de color amarillo
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()

# Ocultamos la tortuga
turtle.hideturtle()

# Oprimir q para salir
onkeypress(bye, "q")
listen()
done()

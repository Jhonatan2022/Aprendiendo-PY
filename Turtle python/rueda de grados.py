#Importamos el modulo.
import turtle
from turtle import onkeypress, bye, done, listen

#Iniciamos turtle y creamos area de dibujo
t = turtle.Turtle ()
s = turtle.Screen ()

#Establecemos el color de fondo
s.bgcolor ("white")
#Velocidad puntero
t.speed(2)

#Posicionamos el puntero
t.penup()
t.goto(-50,60)
t.pendown()
#Determinamos el color de la linea
t.color('black','#0609ec')

#Iniciamos a rellenar
t.begin_fill()
#Dibujamos contornos
t.goto(100,100)
t.goto(100,-100)
t.goto(-50,-60)
t.goto(-50,60)
#Finalizamos rellegno
t.end_fill()

#Cambiamos el color del puntero y lo desplazamos

t.penup()
t.goto(15,100)
t.pendown()
#Cambiamos el grosor de la linea
t.width(8)
t.color("white")
#trazamos una nueva linea
t.goto(15,-100)

#linea horizontal
t.penup()
t.goto(100,0)
t.pendown()
t.goto(-100,0)


onkeypress(bye, 'q')
listen()
done()






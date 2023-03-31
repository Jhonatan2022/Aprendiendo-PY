import turtle as t
import colorsys

t.bgcolor("black")
t.tracer(1000)
h = 0
t.pensize(2)
t.up()
t.goto(-480, -400)
t.down()
t.lt(250)

for i in range(500):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.008
    t.pencolor(c)
    t.lt(i)
    t.fd(3)
    t.fd(5)
    t.write('Hola', font=('Verdana', 20, 'bold'))
t.done()
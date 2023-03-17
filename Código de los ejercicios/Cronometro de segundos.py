# Descripción: Cronometro de segundos
import time

# Definimos la función que nos va a permitir contar los segundos
def countdown(t):

    # Mientras t sea mayor a 0
    while t:

        # Dividimos el tiempo en minutos y segundos
        mins, secs = divmod(t, 60)
        # Definimos el formato de los minutos y segundos
        tiempo = '{:02d}:{:02d}'.format(mins, secs)

        # Imprimimos el tiempo
        print(tiempo, end="/r")

        # Esperamos un segundo
        time.sleep(1)
        t -= 1

    print('Finalizo el tiempo !!')

# Pedimos al usuario que ingrese la cantidad de segundos que quiere que recorra el contador
t = input('Ingrese la cantidad de segundos que quiere que recorra el contador: ')

# Llamamos la función countdown
countdown(int(t))

import math
import numbers
from unittest import result
from colorama import Back, init

print ("Calculando")
def progreso (progress, total):
    #Determinamos cuanto porcentaje queremos que cargue
    porcentaje = 50 * (progress / float(total))
    #Definimos la barra de carga
    #También lo podemos remplazar por la siguiente linea teniendo como resultado la carga pero sin el color
    '''barrra = '|' * int(porcentaje) + '-' * (100 - int (porcentaje))'''
    barrra = (Back.BLUE +' '+ Back.RESET) * int(porcentaje) + '-' * (100 - int (porcentaje))
    #Mostramos la barra junto con el porcentaje
    print (f"\r|{barrra}| {porcentaje:.2f}%", end="\r")

#Gneramos la lista de los valores y la velocidad de carga
numbers = [x * 5 for x in range(500,1000)]

#Guardamos los resultados
resultado = []

for i, x in enumerate (numbers):
    resultado.append(math.factorial(x))
    #Llamamos nuestra función progreso
    progreso(i + 1, len(numbers))
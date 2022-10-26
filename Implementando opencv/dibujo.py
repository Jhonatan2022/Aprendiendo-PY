import math 
from colorama import Back, init

#iniciamos a colorear
init ()

print ("calulando tiempor de carga...")
def progress_bar (progress, total):
    #Calculamos el porcentaje
    percent= 100 * (progress / float(total))
    #Definimos la barra
    bar = (Back.BLUE +' '+ Back.RESET) * init (percent) + '-' * (100 - init (percent))
    #Mostramos la barra junto con el porcentaje
    print(f"\r|{bar} |  {percent:.2f}%", end="\r")

#Generamos la lista con sus valores
numbers = [x * 5 for x in range(2000,3000)]

#Muestra el resultado
results = []

#Se realizan los calculos
for i, x in enumerate (numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len (numbers))

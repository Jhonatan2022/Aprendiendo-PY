# Crearemos un programa que calcule el factorial de un número

# Pedimos el número al usuario
number = int(input("Introduce un número: "))

# Creamos una variable factorial que valga 1
factorial = 1

# Cremos una condicional en caso de que el número sea negativo o ingrese una letra
if number < 0:
    print("Lo siento, el factorial de los números negativos no existe")

    # Creamos una condicional en caso de que el número sea 0
elif number == 0:
    print("El factorial de 0 es 1")

    #Creamos una condicional en caso de que el usuario digite una letra
elif number == str:
    print("Lo siento, el factorial de las letras no existe")
else:
    # Creamos un bucle que vaya desde 1 hasta el número introducido por el usuario
    for i in range(1, number + 1):
        # En cada iteración multiplicamos el número por el valor de la variable factorial
        factorial *= i

    # Imprimimos el resultado
    print("El factorial de {} es {}".format(number, factorial))
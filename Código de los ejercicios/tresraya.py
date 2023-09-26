# Primero creamos el mapeo del tablero Con sus valores en blanco
map = [[" "], [" "], [" "], [" "], [" "], [" "], [" "], [" "], [" "]]


# ------------------------------------------------------------------------------------------------


# Definimos la función que nos va a mostrar el tablero en pantalla
def mostrarmapa():
    # Definimos una variable global para poder modificar y acceder desde cualquier parte del programa
    global map

    # Definimos un contador para que nos muestre el tablero en 3 filas
    contador = 0

    # Recorremos el mapeo
    for coordenada in map:
        # Añadimos 1 al contador
        contador += 1

        # Si el contador llega a 3, significa que ya ha recorrido 3 posiciones y por lo tanto, ha llegado al final de la fila
        if contador == 3:
            print(coordenada)

            # Reseteamos el contador para que vuelva a empezar
            contador = 0
        else:
            # Si no ha llegado al final de la fila, no añadimos un salto de línea
            print(coordenada, end="")
    return


# ------------------------------------------------------------------------------------------------------


# Definimos la función que nos va a permitir introducir los valores en el tablero
def convertir(x, y):
    # Definimos un diccionario con las coordenadas de cada posición
    convertir = {
        0: [1, 1],
        1: [1, 2],
        2: [1, 3],
        3: [2, 1],
        4: [2, 2],
        5: [2, 3],
        6: [3, 1],
        7: [3, 2],
        8: [3, 3],
    }

    # Recorremos el diccionario
    for identifica in convertir:
        # Si las coordenadas introducidas coinciden con las del diccionario, devolvemos la posición
        if convertir[identifica][0] == x and convertir[identifica][1] == y:
            # Devuelve la posición
            return identifica


# ------------------------------------------------------------------------------------------------------


# Definimos la función que nos va a permitir actualizar el tablero
def actualizomapa(posicion, figura):
    # Definimos una variable global para poder modificar y acceder desde cualquier parte del programa
    global map

    # Si la posición está vacía, actualizamos el tablero
    if map[posicion] == [" "]:
        # Actualizamos el tablero
        map[posicion] = [figura]
    else:
        # Si la posición no está vacía, mostramos un mensaje de error
        print("Esta casilla ya se encuentra ocupada, vuelve a intentarlo")
    return


# ------------------------------------------------------------------------------------------------------


# Definimos la función que nos va a permitir comprobar si hay un ganador
def ganador():
    # Casos verticales
    if map[0] == map[3] == map[6] != [" "]:
        # ['x'],[' '],[' '],
        # ['x'],[' '],[' '],
        # ['x'],[' '],[' ']
        print("Ganador %s" % map[0])
        return True

    elif map[1] == map[4] == map[7] != [" "]:
        # [' '],['x'],[' '],
        # [' '],['x'],[' '],
        # [' '],['x'],[' ']
        print("Ganador %s" % map[1])
        return True

    elif map[2] == map[5] == map[8] != [" "]:
        # [' '],[' '],['x'],
        # [' '],[' '],['x'],
        # [' '],[' '],['x']
        print("Ganador %s" % map[2])
        return True

    # Casos horizontales
    elif map[0] == map[1] == map[2] != [" "]:
        # ['x'],['x'],['x'],
        # [' '],[' '],[' '],
        # [' '],[' '],[' ']
        print("Ganador %s" % map[0])
        return True

    elif map[3] == map[4] == map[5] != [" "]:
        # [' '],[' '],[' '],
        # ['x'],['x'],['x'],
        # [' '],[' '],[' ']
        print("Ganador %s" % map[3])
        return True

    elif map[6] == map[7] == map[8] != [" "]:
        # [' '],[' '],[' '],
        # [' '],[' '],[' '],
        # ['x'],['x'],['x']
        print("Ganador %s" % map[6])
        return True

    # Casos diagonales
    elif map[0] == map[4] == map[8] != [" "]:
        # [' '],[' '],['x'],
        # [' '],['x'],[' '],
        # ['x'],[' '],[' ']
        print("Ganador %s" % map[0])
        return True

    elif map[6] == map[4] == map[2] != [" "]:
        # ['x'],[' '],[' '],
        # [' '],['x'],[' '],
        # [' '],[' '],['x']
        print("Ganador %s" % map[6])
        return True

    else:
        # Si no hay ganador, comprobamos si hay empate
        if not [" "] in map:
            # Si no hay casillas vacías, significa que el tablero está lleno y por lo tanto, hay empate
            print("EMPATE")

            # Devolvemos True
            return True

        # Si no hay ganador ni empate, devolvemos False
        return False


# ------------------------------------------------------------------------------------------------------


# Definimos la función que nos va a permitir jugar
def pedirdatos():
    # Definimos una variable global para poder modificar y acceder desde cualquier parte del programa
    while True:
        # Llamamos a la función que nos va a pedir los datos
        try:
            # Pedimos los datos
            x = int(input("Digite la coordenada Y del 1 al 3: "))
            y = int(input("Digite la coordenada X del 1 al 3: "))
            figura = str(input("Introduce 0 para círculo o X: "))

            # Comprobamos que los datos introducidos son válidos
            if x >= 0 and x <= 3 and y >= 0 and x <= 3:
                # Si los datos son válidos, devolvemos los datos
                if figura.lower() == "x" or figura == "0":
                    # Si la figura es válida, devolvemos los datos
                    return x, y, figura
            else:
                # Si los datos no son válidos, mostramos un mensaje de error
                print("Por favor introduce una coordenada válida.")

        # Si los datos introducidos no son válidos, mostramos un mensaje de error
        except:
            print("Por favor introduce un número entero.")


# ------------------------------------------------------------------------------------------------------

# Definimos la función que nos va a permitir mostrar el tablero
if __name__ == "__main__":
    # Definimos una variable global para poder modificar y acceder desde cualquier parte del programa
    while True:
        # Llamamos a la función que nos va a mostrar el tablero
        mostrarmapa()

        # Llamamos a la función que nos va a pedir los datos
        X, Y, FIGURA = pedirdatos()

        # Llamamos a la función que nos va a convertir las coordenadas en posición
        POSICION = convertir(X, Y)

        # Llamamos a la función que nos va a actualizar el tablero
        actualizomapa(POSICION, FIGURA)

        # Llamamos a la función que nos va a comprobar si hay un ganador
        if ganador():
            # Si hay un ganador, mostramos un mensaje de reinicio
            print("\nReinicio del mapa\n")

            # Reiniciamos el mapa
            map = [[" "], [" "], [" "], [" "], [" "], [" "], [" "], [" "], [" "]]

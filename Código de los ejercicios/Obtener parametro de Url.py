# Creamos una función que reciba una URL con parámetros
def valordespuesdemetro(link):
    # Creamos una lista donde se guardarán los valores de la URL
    lista = []

    # Split devuelve una lista con los valores que se encuentran entre los caracteres que se le pasan
    valores = link.split("?")[1].split("&")

    # Creamos un bucle que recorra la lista de valores
    for valordespuesdem in valores:
        # Si el valor despues del "=" es un número, lo añadimos a la lista
        lista.append(valordespuesdem.split("=")[1])

    # Imprimimos el lista
    print(lista)


# Probamos la función con la URL dada en el ejemplo mas otros valores que se pueden agregar
valordespuesdemetro(
    "https://retosdeprogramacion.com?sossa=lesabe&challenge=0&reto=11&random=ladrillos&nombre=jhonatan"
)

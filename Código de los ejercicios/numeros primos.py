# Creamos una función para determinar si un número es primo o no
def es_primo(n):
    """
    Esta función determina si un número es primo o no.
    Devuelve True si es primo y False si no lo es.
    """
    # Si el número es menor a 2, no es primo
    if n < 2:
        return False

    # Si el número es 2, es primo
    for i in range(2, int(n**0.5) + 1):
        # Si el número es divisible por algún número entre 2 y la raíz cuadrada del número, no es primo
        if n % i == 0:
            return False
    return True


# Pedimos al usuario la cantidad de números primos que desea imprimir
cantidad = int(input("Ingrese la cantidad de números primos que desea imprimir: "))

# Creamos una lista vacía para almacenar los números primos encontrados
num_primos = []

num = 2

# Creamos un ciclo para encontrar los números primos
while len(num_primos) < cantidad:
    # Si el número es primo, lo agregamos a la lista
    if es_primo(num):
        # Agregamos el número a la lista
        num_primos.append(num)
    num += 1

# Imprimimos los números primos
for primo in num_primos:
    # Imprimimos los números primos separados por comas
    print(primo, end=", ")

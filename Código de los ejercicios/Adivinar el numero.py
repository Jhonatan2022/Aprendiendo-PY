import random

print("Adivina el número\n", "Tienes 5 intentos")
print()

# función para adivinar el número
def adivinar_numero():
    # generar un número aleatorio entre 1 y 10
    numero = random.randint(1, 10)

    # contador de intentos
    intentos = 0

    # bucle para adivinar el número
    while intentos < 5:
        # capturar el número ingresado
        try:
            # Imprimir el número de intentos
            adivina = int(input("Adivina el número: "))

            # comparar el número ingresado con el generado
            if adivina == numero:
                # si el número es correcto, terminar el bucle
                print("¡Ganaste!")
                break
            # si el número ingresado es mayor al generado imprimir un mensaje
            elif adivina > numero:
                print("El número es más pequeño")
                intentos += 1

            # si el número ingresado es menor al generado imprimir un mensaje
            elif adivina < numero:
                print("El número es más grande")
                intentos += 1

        # si el valor ingresado no es un número entero imprimir un mensaje
        except ValueError:
            print("Solo se permiten números")
            intentos += 1
    # si el número de intentos es igual a 5, terminar el bucle
    else:
        print("Perdiste")
        print("El número era", numero)

adivinar_numero()
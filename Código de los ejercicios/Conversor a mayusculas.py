# Crearemos un conversor de texto a mayúsculas

# Pedimos el texto
texto = input("Introduce el texto a convertir: ")

opcion = int(input("1. para convertir a mayúsculas \n2. para convertir a minúsculas: "))

# Creamos la condicional para validar la opcion
if opcion == 1:
    # Convertimos el texto a mayúsculas
    texto = texto.upper()
    print("El texto convertido es: ", texto)

else:
    # Convertimos el texto a minúsculas
    texto = texto.lower()
    print("El texto convertido es: ", texto)

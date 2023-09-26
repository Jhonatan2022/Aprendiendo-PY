# Creamos una agenda de telefonos
def obtener_agenda():
    # Inicializamos la agenda de contactos
    contactos = {}

    # Creamos un ciclo infinito para agregar contactos
    while True:
        nombre = input("Ingrese un nombre o 2 para terminar: ")

        # Si el nombre está vacío, terminamos el ciclo
        if nombre == "2":
            break

        # Si el nombre ya existe, mostramos un mensaje de error
        if nombre in contactos:
            print("Nombre ya existente")

        # Si el nombre no existe, lo agregamos a la agenda
        else:
            telefono = input(f"Ingrese el teléfono de {nombre}: ")
            contactos[nombre] = telefono
    return contactos


# Creamos una función para imprimir la agenda
def imprimir_agenda():
    # Obtenemos la agenda de contactos
    contactos = obtener_agenda()

    # Imprimimos la agenda de contactos
    for nombre in contactos:
        # Obtenemos el teléfono del contacto
        telefono = contactos[nombre]

        # Imprimimos el nombre y el teléfono del contacto
        print(f"{nombre} tiene el teléfono: {telefono}")


# Creamos la función main para ejecutar el programa con un solo clic
def main():
    imprimir_agenda()


main()

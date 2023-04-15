# Importar librerías
import hashlib


# ----------------------------------------------------------------------------------------------
# Importar módulos
def mostrar_menu(opciones):

    # Función que muestra el menú
    print('Seleccione una opción:')

    # Recorremos el diccionario de opciones
    for clave in sorted(opciones):
        # Mostramos la opción
        print(f' {clave}) {opciones[clave][0]}')


# ----------------------------------------------------------------------------------------------
def leer_opcion(opciones):

    # Función que lee la opción seleccionada
    while (a := input('Opción: ')) not in opciones:

        # Si la opción no es válida, mostramos un mensaje de error
        print('Opción incorrecta, vuelva a intentarlo.')

    # Devolvemos la opción
    return a


# ----------------------------------------------------------------------------------------------
def ejecutar_opcion(opcion, opciones):

    # Función que ejecuta la opción seleccionada
    opciones[opcion][1]()


# ----------------------------------------------------------------------------------------------
# Función que ejecuta el menú
def generar_menu(opciones, opcion_salida):

    # Función que genera el menú
    opcion = None

    # Mientras la opción no sea la de salir, mostramos el menú
    while opcion != opcion_salida:

        # Mostramos el menú
        mostrar_menu(opciones)

        # Leemos la opción seleccionada
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


# ----------------------------------------------------------------------------------------------
def menu_principal():

    # Función que muestra el menú principal
    opciones = {
        '1': ('Contador de números pares e impares', pares),
        '2': ('Encriptar texto', encrip),
        '3': ('Archivo cifrado ', cifrado),
        '4': ('Calcular cuantos polidromos has digitado ', escribir),
        '5': ('Salir', salir)
    }

    # Generamos el menú
    generar_menu(opciones, '5')


# ----------------------------------------------------------------------------------------------
def pares():

    # Lee el primer número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

    impar = 0
    par = 0

    # 0 termina la ejecución.
    while number != 0:

        # Verificar si el número es impar.
        if number % 2 == 1:

            # Incrementar el contador de números impares odd_numbers.
            impar += 1

        else:

            # Incrementar el contador de números pares even_numbers.
            par += 1

        # Leer el siguiente número.
        number = int(input("Introduce un número o escribe 0 para detener: "))

    # Imprimir resultados.
    print("Cuenta de números impares:", impar)
    print("Cuenta de números pares:", par)


# ----------------------------------------------------------------------------------------------
def encrip():

    # El usuario ingresa la contraseña que va a utilizar
    contraseña = input("Digite su ontraseña: ")
    # Se codifica la contraseña y luego se aplica el algoritmo de cifrado
    contraseña_cifrada = hashlib.sha512(contraseña.encode())

    # Se imprime la contraseña cifrada en caracteres hexadecimales
    print("Su contraseña cifrada en hexadecimales es: " +
          contraseña_cifrada.hexdigest())


# ----------------------------------------------------------------------------------------------
def cifrado():

    # El usuario ingresa la la dirección del archivo que va a utilizar
    x = str(input("Dijite la dirección de su archivo: "))

    # Se abre el archivo con la información
    f = open(x)

    # El programa leera las linear del archivo
    lineas = f.readlines()

    # Se crea el objeto de clase hash
    h = hashlib.new('md5')

    # Se recorre cada linea del archivo
    for linea in lineas:

        # Se convierte el string en un byte string
        linea = str.encode(linea)

    # Se agregan las lineas del archivo al objeto hash
    h.update(linea)

    # Se imprime la contraseña cifrada en bits
    print('El resultado en bits del hash es: ' + str(h.digest()))

    # Se imprime la contraseña cifrada en caracteres hexadecimales
    print('El resultado en hexadecimales es: ' + str(h.hexdigest()))


# ----------------------------------------------------------------------------------------------
def escribir():

    # El usuario ingresa la la dirección del archivo que va a utilizar
    print('Este programa contara cuantos digitos numericos has puestro en los strings, escribe fin para terminar y + para hacer un conteo de los digitos')

    # Se inicializan las variables
    lineas = 0
    digitos = "0123456789"
    cantidadDigitos = 0
    cadena = input("Cadena: ")

    # Se crea un ciclo while para que el usuario pueda ingresar las cadenas
    while cadena != "fin":

        # Se crea un ciclo for para que el programa pueda contar los digitos
        for caracter in cadena:

            # Se crea un condicional para que el programa pueda contar los digitos
            if caracter in digitos:

                # Se crea un condicional para que el programa pueda contar los digitos
                cantidadDigitos += 1

        # Se crea un condicional para que el programa pueda contar las lineas
        if cadena == "+":

            # Se crea un condicional para que el programa pueda contar las lineas
            lineas += 1

            # Se imprime la cantidad de digitos que hay en la linea
            print("Aparecen ", cantidadDigitos, " dígitos en la línea")
            # Se inicializan las variables
            cantidadDigitos = 0

        # Se crea un condicional para que el programa pueda contar las lineas
        cadena = input("Cadena: ")

    # Se imprime la cantidad de lineas que hay en el archivo
    print("Se leyeron ", lineas, " líneas completas")


# ----------------------------------------------------------------------------------------------
def salir():

    # Función que muestra el mensaje de salida
    print('Saliendo')

# ----------------------------------------------------------------------------------------------
if __name__ == '__main__':

    # Llamamos a la función principal
    menu_principal()
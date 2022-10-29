import hashlib


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Contador de números pares e impares', pares),
        '2': ('Encriptar texto', encrip),
        '3': ('Archivo cifrado ', cifrado),
        '4': ('Calcular cuantos polidromos has digitado ', escribir),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')

def pares():

    # Lee el primer número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

    impar=0
    par=0
    # 0 termina la ejecución.
    while number != 0:
        # Verificar si el número es impar.
        if number % 2 == 1:
            # Incrementar el contador de números impares odd_numbers.
            impar +=1
        else:
            # Incrementar el contador de números pares even_numbers.
            par +=1
        # Leer el siguiente número.
        number = int(input("Introduce un número o escribe 0 para detener: "))

    # Imprimir resultados.
    print("Cuenta de números impares:", impar)
    print("Cuenta de números pares:", par)

def encrip():

    # El usuario ingresa la contraseña que va a utilizar
    contraseña = input("Digite su ontraseña: ")
    # Se codifica la contraseña y luego se aplica el algoritmo de cifrado
    contraseña_cifrada = hashlib.sha512(contraseña.encode()) 

    # Se imprime la contraseña cifrada en caracteres hexadecimales
    print("Su contraseña cifrada en hexadecimales es: " + contraseña_cifrada.hexdigest())

def cifrado():

    # El usuario ingresa la la dirección del archivo que va a utilizar
    x= str (input("Dijite la dirección de su archivo: "))
    # Se abre el archivo con la información 
    f = open (x)
    # El programa leera las linear del archivo
    lineas = f.readlines ()

    # Se crea el objeto de clase hash
    h = hashlib.new ('md5')
    for linea in lineas:
        # Se convierte el string en un byte string
        linea = str.encode (linea)
    # Se agregan las lineas del archivo al objeto hash
    h.update (linea)

    # Se imprime la contraseña cifrada en bits
    print ('El resultado en bits del hash es: ' + str(h.digest()))

    # Se imprime la contraseña cifrada en caracteres hexadecimales
    print ('El resultado en hexadecimales es: ' + str(h.hexdigest()))

def escribir ():

    print ('Este programa contara cuantos digitos numericos has puestro en los strings, escribe fin para terminar y + para hacer un conteo de los digitos')
    lineas=0
    digitos="0123456789"
    cantidadDigitos=0
    cadena=input("Cadena: ")
    while cadena!="fin":
        for caracter in cadena:
            if caracter in digitos:
                cantidadDigitos+=1
        if cadena=="+":
            lineas+=1
            print("Aparecen ", cantidadDigitos, " dígitos en la línea")
            cantidadDigitos=0
        cadena=input("Cadena: ")
    print("Se leyeron ",lineas," líneas completas")
    
def salir():
    print('Saliendo')

if __name__ == '__main__':
    menu_principal()
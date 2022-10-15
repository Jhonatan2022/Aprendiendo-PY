# Se importa hashlib
import hashlib


def encriptar(x):

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
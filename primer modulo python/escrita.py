# Se importa hashlib
import hashlib


def encriptar(contraseña):

    # Se codifica la contraseña y luego se aplica el algoritmo de cifrado
    contraseña_cifrada = hashlib.sha512(contraseña.encode()) 

    # Se imprime la contraseña cifrada en caracteres hexadecimales
    print("Su contraseña cifrada en hexadecimales es: " + contraseña_cifrada.hexdigest())
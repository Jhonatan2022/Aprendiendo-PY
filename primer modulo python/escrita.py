# Se importa hashlib
import hashlib


def encriptar(contraseña):

    contraseña_cifrada = hashlib.sha512(contraseña.encode()) 

    print("Su contraseña cifrada en hexadecimales es: " + contraseña_cifrada.hexdigest())